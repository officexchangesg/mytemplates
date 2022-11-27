from django.contrib import admin
from DJ.admin import admin_site
# from django.utils.html import escape, strip_tags
from .models import DJ_Snippet, DJ_Concept, DJ_Howto
# Register your models here.


@admin.register(DJ_Snippet, site=admin_site)
class DJ_Model_Field_Admin(admin.ModelAdmin):
    list_display = ['title', 'snippet']


@admin.register(DJ_Howto, site=admin_site)
class DJ_How_To_Admin(admin.ModelAdmin):
    list_display = ['howto', 'description']


@admin.register(DJ_Concept, site=admin_site)
class DJ_Concept_Admin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_Concept_Clear']


