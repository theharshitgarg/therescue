from django.db import models
from django.utils import timezone

# Create your models here.


class Rescuer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	user_id = models.CharField(max_length=100)
	location = models.CharField(max_length=50)
	no_of_animals_rescued = models.IntegerField(default=0)

	def __str__(self):
		return self.first_name+' '+self.last_name


class Animal(models.Model):
	category = models.CharField(max_length=50)
	found_at = models.CharField(max_length=50)
	found_on = models.DateTimeField('found_on')
	is_injured = models.BooleanField(default=False)
	is_handicapped = models.BooleanField(default=False)

	def __str__(self):
		return self.first_name+' '+self.last_name


class RescueOperation(models.Model):
	started_at = models.CharField(max_length=200)
	started_on = models.DateTimeField('started_on')
	started_by = models.CharField(max_length=200)
	closed_at = models.CharField(max_length=200)
	closed_on = models.DateTimeField('closed_on')
	treated_at = models.CharField(max_length=200)
	rescue_id = models.IntegerField(primary_key=True)


