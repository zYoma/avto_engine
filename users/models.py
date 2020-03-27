from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

class ConfirmationCode(models.Model):
    code = models.UUIDField( default=uuid.uuid4, editable=False, verbose_name=_("Код подтверждения"))
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_confirm_code', verbose_name=_("Пользователь"))

    def __str__(self):
        return str(self.code)

    class Meta:
        verbose_name = 'Код подтверждения регистрации'
        verbose_name_plural = "Коды подтверждения регистрации"


# @receiver(pre_save, sender=User)
# def user_updated(sender, **kwargs):
#     user = kwargs.get('instance', None)
#     if user:
#         new_password = user.password
#         try:
#             old_password = User.objects.get(pk=user.pk).password
#         except User.DoesNotExist:
#             old_password = None
#         if new_password != old_password:
#         # do what you need here