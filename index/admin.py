from django.contrib import admin
from . models import About
from . models import Services
from . models import Projects
from . models import Contact
# Register your models here.
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(Contact)