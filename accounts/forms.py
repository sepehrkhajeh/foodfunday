from django import forms
from django.core.exceptions import ValidationError
from .models import UserModel



class UserForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder': 'تاید رمزعبور'}))
    name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': ' نام خانوادگی'}))
    phone = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'شماره تلفن'}))
    
    class Meta:
        model = UserModel
        fields = (
            'name',
            'last_name',
            'phone',
            'password1',
            'password2',
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("رمز عبور باهم مطابقت ندارند")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
