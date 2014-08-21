from django.db import models

# Create your models here.
class Categories(models.Model):

	name = models.CharField(max_length = 45) # name_using_under_score
	description = models.CharField(max_length = 50) # Pretty Name to display 
	deleted = models.BooleanField(default = False)


class Tables(models.Model):

	name = models.CharField(max_length = 45) # using_under_score
	description = models.CharField(max_length = 90) # Name for Display
	category = models.CharField(max_length = 45) # this matches the name field on the Categories table: uses_dashes
	deleted = models.BooleanField(default = False)

#prm_trcks_added
class prm_trcks_added(models.Model):

	year = models.IntegerField()
	month = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True,null=True)
	prm_trcks_added = models.IntegerField()
	customers = models.IntegerField()

class prm_albms_added(models.Model):

	year = models.IntegerField()
	month = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True, null=True)
	prm_albms_added = models.IntegerField()
	customers = models.IntegerField()

class prm_plst_added(models.Model):

	year = models.IntegerField()
	month = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True, null=True)
	prm_plst_added = models.IntegerField()
	customers = models.IntegerField()

 