from django import forms
from .models import Order

# copied from ckz8780

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)   # super call the default init method to set up form as it would be by default
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True    # starts the full name field when user loads page
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'  # star if requierd field
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder   # placeholder attr. to their values in dictionary above
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False   # removing the form fields labels