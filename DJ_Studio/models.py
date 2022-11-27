from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class DJ_Model_Field(models.Model):
    field_type = models.CharField(verbose_name='Field Type', max_length=100)
    # desc = models.TextField(verbose_name='Description', blank=True,null=True)
    description = HTMLField()

    class Meta:
        verbose_name = 'Model Field'
        verbose_name_plural = 'Model Fields'

    def __str__(self):
        return self.field_type


class DJ_Relationship_Field(models.Model):
    field_type = models.CharField(verbose_name='Field Type', max_length=100)
    # desc = models.TextField(verbose_name='Description', blank=True,null=True)
    description = HTMLField()

    class Meta:
        verbose_name = 'Relationship Field'
        verbose_name_plural = 'Relationship Fields'


class DJ_Model_Field_Attribute(models.Model):
    VALUE_TYPE_CHOICES = (
        ('', '-- Make A Choice --'),
        ('str', 'String'),
        ('int', 'Integer'),
        ('obj', 'Object'),
        ('set', 'Set'),
        ('bol', 'Boolean'),
        ('lst', 'List'),
    )
    name = models.CharField(verbose_name='Field Attribute', max_length=100)
    value_type = models.CharField(max_length=3, choices=VALUE_TYPE_CHOICES, blank=False)
    description = HTMLField()
    fields = models.ManyToManyField(DJ_Model_Field, null=True, db_table='model_attribute_field_mapping_table')

    class Meta:
        verbose_name = 'Model Field Attribute'
        verbose_name_plural = 'Model Field Attributes'
