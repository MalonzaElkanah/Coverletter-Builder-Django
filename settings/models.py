from django.db import models
from django.urls import reverse

# Create your models here.
import os

class BaseModel(models.Model):
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	class Meta:
		abstract = True
		ordering=("id",)


class Letter(BaseModel):
	name = models.CharField('CV Name', max_length=50)
	file = models.FileField(upload_to='uploads/document/cover_letters/', max_length=1000)
	text = models.TextField(null=True)
	description = models.TextField(null=True)
	# name, file, text, description, status,

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('letters')

	def file_extension(self):
		path = self.file.path
		file_name = os.path.basename(path)
		file_dictionary = file_name.split('.')
		file_extension = file_dictionary[-1]
		return file_extension


class UserProfile(BaseModel):
	title = models.CharField('Title', max_length=150, null=True)
	first_name = models.CharField('First Name', max_length=50)
	middle_name = models.CharField('Middle Name', max_length=50, null=True)
	last_name = models.CharField('Last Name', max_length=50, null=True)
	email = models.CharField('Email', max_length=50, null=True)
	phone_number = models.CharField('Phone Number', max_length=50, null=True)
	location = models.CharField('Location', max_length=50, null=True)
	# title, first_name, middle_name, last_name, email, phone_number, location

	def get_absolute_url(self):
		return reverse('user-profiles')


class JobProfile(BaseModel):
	name = models.CharField('Name', max_length=200)
	experience = models.CharField('Experience', max_length=200, null=True)
	description = models.TextField('Description', null=True)
	organization = models.CharField('Organization', max_length=200)
	address = models.TextField('Address', null=True)
	email = models.CharField('Link', max_length=1000, null=True)
	# name, experience, description, organization, address, email

	def get_absolute_url(self):
		return reverse('job-profiles')

	def __str__(self):
		return self.name

	def qualifications(self):
		return Qualification.objects.filter(job=self.id)

	def attributes(self):
		return Attribute.objects.filter(job=self.id)


class Qualification(BaseModel):
	job = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
	name = models.CharField('Qualification', max_length=500)
	# job, name


class Attribute(BaseModel):
	job = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
	name = models.CharField('Attribute', max_length=500)
	# job, name
