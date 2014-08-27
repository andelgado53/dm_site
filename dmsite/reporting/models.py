from django.db import models

# Create your models here.
class Categories(models.Model):

	name = models.CharField(max_length = 45) # name_using_under_score
	description = models.CharField(max_length = 50) # Pretty Name to display 
	deleted = models.BooleanField(default = False)
	
	class Meta:
		db_table = 'Categories'
		ordering = ['name']


class Tables(models.Model):

	name = models.CharField(max_length = 45) # using_under_score
	description = models.CharField(max_length = 90) # Name for Display
	category = models.CharField(max_length = 45) # this matches the name field on the Categories table: uses_dashes
	deleted = models.BooleanField(default = False)

	class Meta:
		db_table = 'Tables'
		ordering = ['description']

#prm_trcks_added
class prm_trcks_added(models.Model):

	year = models.IntegerField()
	month = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True,null=True)
	prm_trcks_added = models.IntegerField()
	customers = models.IntegerField()

	def __unicode__(self):
		return str(self.year) + '-' + str(self.month) + '-' +str(self.week)

	class Meta:
		db_table = 'prm_trcks_added'
		ordering = ['-month', '-week']

class prm_albms_added(models.Model):

	year = models.IntegerField()
	month = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True, null=True)
	prm_albms_added = models.IntegerField()
	customers = models.IntegerField()

	def __unicode__(self):
		return str(self.year) + '-' + str(self.month) + '-' +str(self.week)

	class Meta:
		db_table = 'prm_albms_added'
		ordering = ['-month', '-week']

class prm_plst_added(models.Model):

	year = models.IntegerField()
	month = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True, null=True)
	prm_plst_added = models.IntegerField()
	customers = models.IntegerField()

	def __unicode__(self):
		return str(self.year) + '-' + str(self.month) + '-' +str(self.week)

	class Meta:
		db_table = 'prm_plst_added'
		ordering = ['-month', '-week']


class gms_units(models.Model):
	
	year = models.IntegerField()
	month = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True, null=True)
	gms = models.DecimalField(decimal_places = 2, max_digits=12)
	units = models.IntegerField()
	customers = models.IntegerField()

	def __unicode__(self):
		return str(self.year) + '-' + str(self.month) + '-' +str(self.week)

	class Meta:
		db_table = 'gms_units'
		ordering = ['-month', '-week']

class vendor_gms(models.Model):

	year = models.IntegerField()
	month = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True, null=True)
	vendor_name = models.CharField(max_length=30)
	gms = models.DecimalField(decimal_places = 2, max_digits=12)
	units = models.IntegerField()
	customers = models.IntegerField()

	def __unicode__(self):
		return str(self.year) + '-' + str(self.month) + '-' +str(self.week)

	class Meta:
		db_table = 'vendor_gms'
		ordering = ['-month', '-week']

class avg_strmg_hrs(models.Model):

	year = models.IntegerField()
	month = models.IntegerField(blank=True, null=True)
	week = models.IntegerField(blank=True, null=True)
	avg_strmg_hrs = models.DecimalField(decimal_places = 2, max_digits=4)

	def __unicode__(self):
		return str(self.year) + '-' + str(self.month) + '-' +str(self.week)

	class Meta:
		db_table = 'avg_strmg_hrs'
		ordering = ['-month', '-week']






