from django.contrib import admin
from .models import newcases, recovery, deaths, vaccine

# Register your models here.

admin.site.register(newcases)
admin.site.register(recovery)
admin.site.register(deaths)
admin.site.register(vaccine)