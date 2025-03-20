from django.contrib import admin
from .models import Applicant
# Register your models here.

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address','status')
    search_fields = ('name', 'email')
    list_filter = ('age')
    ordering = ('-id')
admin.site.register(Applicant, ApplicantAdmin)