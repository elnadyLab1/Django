from django.db import models

# Create your models here.

class BaseModel(models.Model):
  create_date = models.DateTimeField(auto_now_add=True, editable=False)
  last_updated = models.DateTimeField(auto_now=True, editable=False)

  class Meta:
    abstract = True
