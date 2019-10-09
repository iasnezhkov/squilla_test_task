from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Page(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return '{id} {name}'.format(name=self.name, id=self.id)

    def __unicode__(self):
        return u'{id} {name}'.format(name=self.name, id=self.id)
