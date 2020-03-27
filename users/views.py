from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import CreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
import uuid
from .models import ConfirmationCode
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

User = get_user_model()

class SignUp(CreateView):
    form_class = CreationForm
    template_name = "users/signup.html"

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        new_user.groups.add(Group.objects.get(name='user'))
        new_user.is_active = False 
        new_user.save()
        uuid_pass = uuid.uuid4()
        new_confirm_code = ConfirmationCode.objects.create(user = new_user, code = uuid_pass)
        email = form.cleaned_data['email']
        send_mail_ls(email, new_user, uuid_pass)
        # login(self.request, new_user)
        return valid

    def get_success_url(self):
        return reverse('confirm')

def send_mail_ls(email, new_user, uuid_pass):
    url = f'http://176.57.215.48:5001/auth/confirm-email/{uuid_pass}/{new_user.username}/'
    send_mail('Подтверждение регистрации', f'Для подтверждения регистрации перейдите по ссылке {url}', 'Авто <admin@gafuk.ru>',[email], fail_silently=False)



class ConfirmEmail(View):
    def get(self, request, uuid_pass, username):
        try:
            user = User.objects.get(username = username)
            code = ConfirmationCode.objects.get(user = user, code = uuid_pass)
        except:
            return HttpResponse('<h1>Не верный код подтверждения!</h1>')
        else:   
            user.is_active = True
            user.save()
            code.delete()

        return redirect('/auth/login/')


class ConfirmEmailTemplate(View):
    def get(self, request):
        return render(request, 'users/confirm_registration.html')