# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SingleQuery.direction'
        db.add_column(u'bustracker_singlequery', 'direction',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SingleQuery.direction'
        db.delete_column(u'bustracker_singlequery', 'direction')


    models = {
        u'bustracker.singlequery': {
            'Meta': {'object_name': 'SingleQuery'},
            'bus_line_id': ('django.db.models.fields.IntegerField', [], {}),
            'bus_stop_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query_successful': ('django.db.models.fields.BooleanField', [], {}),
            'time_remaining': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['bustracker']