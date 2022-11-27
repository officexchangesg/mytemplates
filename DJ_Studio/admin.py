from django.contrib import admin
from DJ.admin import admin_site
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import DJ_Model_Field, DJ_Model_Field_Attribute, DJ_Relationship_Field
# Register your models here.


@admin.register(DJ_Model_Field, site=admin_site)
class DJ_Model_Field_Admin(admin.ModelAdmin):
    list_display = ['field_type', 'description']


@admin.register(DJ_Relationship_Field, site=admin_site)
class DJ_Relationship_Field_Admin(admin.ModelAdmin):
    list_display = ['field_type', 'description']


@admin.register(DJ_Model_Field_Attribute, site=admin_site)
class DJField_Attribute_Admin(admin.ModelAdmin):
    # list_display = ['name', 'value_type']
    list_display = ['name', 'value_type', 'description']
    formfield_overrides = {
        models.ManyToManyField: {
            "widget": CheckboxSelectMultiple(attrs={'class': 'checkbox_css'}),
        },
    }

