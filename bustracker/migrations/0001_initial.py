# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'singleQuery'
        db.create_table(u'bustracker_singlequery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('bus_line_id', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_stop_id', self.gf('django.db.models.fields.IntegerField')()),
            ('query_successful', self.gf('django.db.models.fields.BooleanField')()),
            ('time_remaining', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'bustracker', ['singleQuery'])


    def backwards(self, orm):
        # Deleting model 'singleQuery'
        db.delete_table(u'bustracker_singlequery')


    models = {
        u'bustracker.singlequery': {
            'Meta': {'object_name': 'singleQuery'},
            'bus_line_id': ('django.db.models.fields.IntegerField', [], {}),
            'bus_stop_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query_successful': ('django.db.models.fields.BooleanField', [], {}),
            'time_remaining': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['bustracker']