# from django.shortcuts import render, redirect
# from authentication.forms import UserRegistrationForm
# from django.contrib.auth import login, authenticate
# from django.contrib import messages
# from django.shortcuts import render, get_object_or_404
# from cart.forms import CartAddProductForm
# from .models import Category, Product

# # Create your views here.

# def register(request):
#     if request.method == 'POST' :
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request,user)
#             messages.success(request, f'félicitation {username}, Votre compte a été créé avec succès !')
#             return redirect('home')
#     else :
#         form = UserRegistrationForm()
#     return render(request, 'registration/register.html', {'form' : form})
