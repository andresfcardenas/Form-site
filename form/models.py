#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class ModelContact(models.Model):
	"""
	Este es el modelo para el formulario
	"""
	
	name = models.CharField(max_length=50)
	phone = models.IntegerField(max_length=7, null=True, blank=True)
	asunto = models.CharField(max_length=50)
	message = models.TextField(max_length=200)
	
	def __unicode__(self):
		return self.asunto
