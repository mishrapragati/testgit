from django.db import models
from django.db import models
# Create your models here.
class emp(models.Model):
    empno = models.IntegerField()
    empname = models.TextField()
    empcontactno = models.DecimalField()