from django.db import models

# Create your models here.
class cou(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, default='')
    inter_data = models.TextField(max_length=4000, default='')

    def __str__(self):
        return self.name

class sta(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, default='')
    country_id = models.IntegerField()
    inter_data = models.TextField(max_length=4000, default='')

    def __str__(self):
        return self.name+'_'+str(self.country_id)

class cit(models.Model):
    id = models.IntegerField(primary_key=True)
    state_id = models.IntegerField()
    country_id = models.IntegerField()
    name = models.CharField(max_length=200, default='')
    inter_data = models.TextField(max_length=4000, default='')

    def __str__(self):
        return self.name+'_'+str(self.country_id)