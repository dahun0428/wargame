from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import ast


class ListField (models.TextField):

#  __metaclass__ = models.
  description = "Stores a python list"

  def __init__ (self, *args, **kwargs):
    super (ListField, self).__init__(*args, **kwargs)

  def frm_db_value (self, value, expression, connection, context):
    if value is None:
      return value
    return parse_hand (value)

  def to_python (self, value):
    if not value:
      value = []
    if isinstance (value, list):
      return value

    return ast.literal_eval (value)

  def get_prep_value (self, value):
    if value is None:
      return value
    
    return unicode (value)

  def value_to_string (self, obj):
    value = self._get_val_from_obj (obj)
    return self.get_db_prep_value (value)


class UserProfile (models.Model):

  user = models.OneToOneField (User)
  nickname = models.CharField (max_length = 30)
  user_score = models.IntegerField ()
  user_solved = ListField ()
  user_comment = models.CharField (max_length = 100)


  def __str__ (self):
    return self.user_nickname 


  def register (self):
    self.registerDate = timezone_now ()
    self.save ()


