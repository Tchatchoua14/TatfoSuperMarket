from django.contrib import admin
from .models import Category, Product, Livraison, Cart, BillingDetails, Order, Newsletters
# , Verification

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    ordering = ('-created',)
    prepopulated_fields = {'slug': ('name',)}


class BillingDetailsInline(admin.TabularInline):
    model = BillingDetails
    raw_id_fields = ['product']

# @admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'phone', 'company', 'apartment', 'post_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [BillingDetailsInline]


from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']

@admin.register(Livraison)
class LivraisonAdmin(admin.ModelAdmin):
    list_display = ['nom', 'frais']

admin.site.register(Coupon, CouponAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', )


admin.site.register(Cart, CartAdmin)
admin.site.register(BillingDetails)
admin.site.register(Order)

@admin.register(Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
    list_display = ['email', 'created']

# @admin.register(Verification)
# class VerificationAdmin(admin.ModelAdmin,):
# 	list_display = ['id', 'token','user', 'verify']
