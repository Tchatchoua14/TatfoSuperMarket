from django.contrib import admin
from .models import Profile


admin.site.register(Profile)

# @admin.register(Verification)
# class VerificationAdmin(admin.ModelAdmin,):
# 	list_display = ['id', 'token','user', 'verify']