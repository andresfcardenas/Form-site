#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import ModelContact

class FormContact(ModelForm):
	"""
	Es el formulario de contacto :D
	"""
	class Meta():
		model = ModelContact
		
		fields = (
		'name',
		'phone',
		'asunto',
		'message'
		)
