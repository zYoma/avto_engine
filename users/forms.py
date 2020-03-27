from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()

class CreationForm(UserCreationForm):
    error_css_class = 'error'
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")


    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if email == '':
            raise forms.ValidationError('Необходимо указать email!')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Данный email уже есть в БД!')
        return email
