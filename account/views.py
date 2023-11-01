from django.shortcuts import render, redirect, get_object_or_404
from account.forms import RegisterForm, CustomLoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetView,
     PasswordResetDoneView,
    LoginView)
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views import View
from captcha.fields import ReCaptchaField
# from cart.forms import CartAddProductForm
# from .models import Category, Product

# # Create your views here.

# class UserLoginView(LoginView):
#     template_name = 'registration/login.html'
#     form_class = LoginForm

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('Ecommerce:home')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            
        return super(RegisterView, self).form_valid(form)

# def register(request):
#     if request.method == 'POST' :
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request,user)
#             messages.success(request, f'félicitation {username}, Votre compte a été créé avec succès !')
#             return redirect('Ecommerce:home')
#     else :
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form' : form})


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('Ecommerce:home') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


# class RegistrationView(CreateView):
#     template_name = 'registration/register.html'
#     # form_class = RegisterForm
#     form_class = CustomUserCreationForm
#     # success_url = 'login'
#     success_url = reverse_lazy('account:login')

def logout_view(request):
    logout(request)
    return redirect(reverse('account:login'))

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class MyPasswordResetDoneView(PasswordResetDoneView):
     template_name = 'registration/password_reset_done.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('password_change_done')

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_comfirm')

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_email.html'

# class Home(TemplateView):
#     template_name = 'index.html' 

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["username"] = self.request.user.username
#         return context


class MyProfile(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        
        return render(request, 'registration/profile.html', context)
    
    def post(self,request):
        user_form = UserUpdateForm(
            request.POST, 
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request,'Your profile has been updated successfully')
            
            return redirect('account:profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request,'Error updating you profile')
            
            return render(request, 'registration/profile.html', context)
            
    