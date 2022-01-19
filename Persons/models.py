from django.db import models
from GraphQL.models import BaseModel, BaseModelName, BaseModelNative
from Utils.models import Gender, Job, Title
# Create your models here.


class Person(BaseModel):
  national_id = models.SmallIntegerField(unique=True)
  full_name = models.CharField(max_length=50, unique=True)
  family_name = models.CharField(max_length=10)
  birth_date = models.DateField()
  image_url = models.ImageField(
      upload_to="images", editable=True, null=True, blank=True
  )
  gender = models.ForeignKey(
      Gender, on_delete=models.SET_NULL, related_name="persons"
  )
  Job = models.ForeignKey(Job, on_delete=models.SET_NULL, related_name="persons")
  title = models.ForeignKey(Title, on_delete=models.SET_NULL, related_name="persons")
  

class Doctor():
  pass


class Patient():
  pass


class Customer():
  pass


class Employee():
  pass


class User():
  pass