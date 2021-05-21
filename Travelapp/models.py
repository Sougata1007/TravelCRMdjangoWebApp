from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=200,null = True)
	phone = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.name


class Packages(models.Model):
	CATEGORY = (
			('Group','Group'),
			('Solo','Solo'),
			('Trekking','Trekking')
		)

	pack_name = models.CharField(max_length=200,null=True)
	tripduration = models.CharField(max_length=200,null=True)
	destination = models.CharField(max_length=1000,null=True)
	price = models.FloatField(null=True)
	date_created = models.DateTimeField(auto_now_add= True,null=True)
	category = models.CharField(max_length=200,null=True,choices = CATEGORY)
	tags=models.ManyToManyField(Tag)

	def __str__(self):
		return self.pack_name

class Order(models.Model):
	STATUS = (
		('Completed','Completed'),
		('Tripping','Tripping'),
		('Pending','Pending')
		)


	customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
	packages = models.ForeignKey(Packages,null=True,on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True,null=True)
	status = models.CharField(max_length=200,null=True,choices = STATUS)
	note = models.CharField(max_length=1000,null=True)

	
	def __str__(self):
		return self.packages.pack_name
	