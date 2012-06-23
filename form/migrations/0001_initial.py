# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModelContact'
        db.create_table('form_modelcontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=7, null=True, blank=True)),
            ('asunto', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal('form', ['ModelContact'])


    def backwards(self, orm):
        # Deleting model 'ModelContact'
        db.delete_table('form_modelcontact')


    models = {
        'form.modelcontact': {
            'Meta': {'object_name': 'ModelContact'},
            'asunto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['form']