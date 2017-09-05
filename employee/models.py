# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=50)
    height = models.IntegerField(default=10)


class Hobbies(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hobby = models.CharField(max_length=200)
    
