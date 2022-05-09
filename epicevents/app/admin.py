from django.contrib import admin
from . import models


# Register your models here.


admin.site.register(models.Employee)
admin.site.register(models.Customer)
admin.site.register(models.Prospect)

admin.site.register(models.Provider)

admin.site.register(models.Contract)
admin.site.register(models.Event)
