from django.contrib import admin

# Register your models here.
from edApp.models import edsystango,ClassesForm,InstituteForm,rulesForm,feesForm


admin.site.register(edsystango)
admin.site.register(ClassesForm)
admin.site.register(InstituteForm)
admin.site.register(rulesForm)
admin.site.register(feesForm)