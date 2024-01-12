from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import MyProfile, RegisterView
# from django.contrib.auth.views import (
#     PasswordResetView, 
#     PasswordResetDoneView, 
#     PasswordResetConfirmView,
#     PasswordChangeView,
#     PasswordResetCompleteView
# )

app_name = 'accountss'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html', html_email_template_name='registration/password_reset_email.html'), name="password_reset"),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name="password_change_done"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
    path('register/', RegisterView.as_view(), name='register'),
    path('delete_account/', views.delete_account, name="delete_account"),
    path('profile/', MyProfile.as_view(), name='profile'),
     # path('account-verify/<slug:token>', views.account_verify, name="account-verify"),
]


