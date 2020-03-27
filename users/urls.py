from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("confirm-email/<str:uuid_pass>/<str:username>/", views.ConfirmEmail.as_view(), name="confirm_email_url"),
    path("confirm-registration/", views.ConfirmEmailTemplate.as_view(), name="confirm"),
    ]
