from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DtokUser
from .forms import DtokUserChangeForm, DtokUserCreationForm

# Register your models here.
class CustomeUserAdmin(UserAdmin):
    add_form = DtokUserCreationForm
    form = DtokUserChangeForm
    model = DtokUser
    list_display = ('email', 'display_name','phone_number','is_active','is_staff')
    list_filter = ('email', 'is_active',)
    fieldsets = (
        ('Thông tin', {'fields': ('email', 'password', 'display_name','avatar')}),
        ('Trạng thái', {'fields': ('is_active','is_staff')}),
    )
    add_fieldsets = (
        ('Thông tin', {'fields': ('email', 'password1', 'password2', 'display_name','avatar')}),
        ('Trạng thái', {'fields':('is_active','is_staff')})
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(DtokUser, CustomeUserAdmin)