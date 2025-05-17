from django import forms
from django_select2.forms import Select2Widget
from .models import UserInfo

# O‘zbekiston hududlari
UZBEKISTAN_REGIONS = [
    ("Andijon", "Andijon"),
    ("Buxoro", "Buxoro"),
    ("Farg'ona", "Farg'ona"),
    ("Jizzax", "Jizzax"),
    ("Xorazm", "Xorazm"),
    ("Namangan", "Namangan"),
    ("Navoiy", "Navoiy"),
    ("Qashqadaryo", "Qashqadaryo"),
    ("Qoraqalpog'iston", "Qoraqalpog‘iston Respublikasi"),
    ("Samarqand", "Samarqand"),
    ("Sirdaryo", "Sirdaryo"),
    ("Surxondaryo", "Surxondaryo"),
    ("Toshkent", "Toshkent shahri"),
    ("Toshkent viloyati", "Toshkent viloyati"),
]


class UserInfoForm(forms.ModelForm):
    region = forms.ChoiceField(
        choices=UZBEKISTAN_REGIONS,
        widget=Select2Widget(
            attrs={"class": "form-control", "data-placeholder": "Viloyatni tanlang..."}
        ),
        label="Viloyatingiz",
    )

    class Meta:
        model = UserInfo
        fields = ["full_name", "phone_number", "region"]
        labels = {
            "full_name": "To'liq Ismingiz",
            "phone_number": "Telefon Raqamingiz",
        }
