from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key= True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    phone=models.IntegerField()

    class Meta:
        unique_together = ('first_name', 'last_name',)

    def __unicode__(self):
        return self.first_name + " " + self.last_name + " - " + str(self.phone)