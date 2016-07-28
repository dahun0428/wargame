#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Problem (models.Model):
  prob_title = models.CharField (max_length=200)
  prob_description = models.TextField ()
  created_date = models.DateTimeField (default=timezone.now)
  prob_score = models.IntegerField ()
  prob_flag = models.CharField (max_length = 100)
  prob_image = models.ImageField ()
  prob_file = models.FileField ()

  def __str__ (self):
    return self.prob_title

  def publish (self):
    self.publish_date = timezone_now ()
    self.save ()

