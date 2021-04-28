from .models import DtokUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class DtokUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = DtokUser
        fields = ('email','display_name','is_active')


class DtokUserChangeForm(UserChangeForm):

    class Meta:
        model = DtokUser
        fields = ('email','display_name','is_active')