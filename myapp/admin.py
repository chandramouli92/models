from django.contrib import admin
from myapp import models

# Register your models here.
class TopicAdminView(admin.ModelAdmin):
    list_display=('Topic_name')
    search_fields=('Topic_name')
class WebpageAdminView(admin.ModelAdmin):
    list_display=('Topic','name','url')
    search_field=('Topic','name')
    list_editable=('name')
    list_filter=('Topic')
class AccessDetailsAdminView(admin.ModelAdmin):
    list_display=('Webpage','datetime')
    search_fields=('Webpage','datetime')
admin.site.register(models.Topic)
admin.site.register(models.Webpage)
admin.site.register(models.AccessDetails)