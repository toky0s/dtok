from sre_compile import dis
from django import forms
from django.contrib.auth.models import User
from users.models import DtokUser
import re

class RegisterForm(forms.Form):

    email = forms.EmailField(label='Email', widget=forms.EmailInput(), label_suffix="")
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(), label_suffix="")
    repassword = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput(), label_suffix="")
    display_name = forms.CharField(label='Tên hiển thị',label_suffix="")
    phone_number = forms.CharField(label='Số điện thoại',label_suffix="")

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", email):
            raise forms.ValidationError('Email không hợp lệ')
        try:
            DtokUser.objects.get(email=email)
        except DtokUser.DoesNotExist:
            return email
        raise forms.ValidationError('Email này đã tồn tại')

    def clean_display_name(self):
        display_name = self.cleaned_data['display_name']
        if not re.search("[A-Za-z0-9_]{0,30}", display_name):
            raise forms.ValidationError('Tên hiển thị không hợp lệ')
        try:
            DtokUser.objects.get(display_name=display_name)
        except:
            return display_name
        raise forms.ValidationError('Tên này đã tồn tại')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) != 10:
            raise forms.ValidationError('Số điện thoại là một dãy 10 số')
        try:
            DtokUser.objects.get(phone_number=phone_number)
        except:
            return phone_number
        raise forms.ValidationError('Số điện thoại này đã tồn tại trên hệ thống')

    def clean_password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$",password):
                raise forms.ValidationError('Mật khẩu không hợp lệ')
            return password

    def clean_repassword(self):
        if 'password' in self.cleaned_data:
            repassword = self.cleaned_data['repassword']
            password = self.cleaned_data['password']
            if not repassword == password:
                raise forms.ValidationError('Mật khẩu nhập lại không khớp')
            return repassword

    def save(self):
        DtokUser.objects.create_user(
            email=self.cleaned_data['email'],
            password = self.cleaned_data['password'],
            display_name = self.cleaned_data['display_name'],
            phone_number = self.cleaned_data['phone_number'])