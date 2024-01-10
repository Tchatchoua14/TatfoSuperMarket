from django import forms
from .models import BillingDetails, Newsletters


class BillingDetailsForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'company', 'apartment', 'post_code', 'city']

class CouponApplyForm(forms.Form):
    code = forms.CharField()

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class NewlettersForm(forms.ModelForm):
    class Meta: 
        model = Newsletters
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data["email"]
            return email 
        
