from django.contrib import admin
from mywebsite.models import *

# Register your models here.
class JobsAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/admin.css", )
        }

        js =  ("js/blog.js", )
        
admin.site.register(Jobs, JobsAdmin)
admin.site.register(Contact)
