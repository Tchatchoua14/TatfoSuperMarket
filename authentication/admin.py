from django.contrib import admin

# Register your models here.
# from .models import Category, Product

# #register
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'price', 'available', 'created']
#     list_filter = ['available', 'created', 'updated']
#     list_editable = ['price', 'available']
#     prepopulated_fields = {'slug': ('name',)}

# class CouponAdmin(admin.ModelAdmin):
#     list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
#     list_filter = ['active', 'valid_from', 'valid_to']
#     search_fields = ['code']

# admin.site.register(Coupon, CouponAdmin)