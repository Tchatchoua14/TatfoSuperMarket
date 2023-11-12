from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisterView, MyProfile

app_name = 'account'


urlpatterns = [
    # path('', views.Home.as_view(template_name='index.html'), name='home1'),
    # path("change-password/", auth_views.PasswordChangeView.as_view()),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html', html_email_template_name='registration/password_reset_email.html'), name="password_reset"),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name="password_change_done"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', MyProfile.as_view(), name='profile'),
]


    # path('register/', views.register, name="register"),
    # path('register/', views.RegistrationView.as_view(template_name='registration/register.html'), name="register"),

    #  path('login/', MyLoginView.as_view(redirect_authenticated_user=True),name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'),name='logout'),

