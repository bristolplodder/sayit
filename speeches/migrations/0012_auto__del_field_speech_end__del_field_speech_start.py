# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Speech.end'
        db.delete_column('speeches_speech', 'end')

        # Deleting field 'Speech.start'
        db.delete_column('speeches_speech', 'start')


    def backwards(self, orm):
        # Adding field 'Speech.end'
        db.add_column('speeches_speech', 'end',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Speech.start'
        db.add_column('speeches_speech', 'start',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    models = {
        'speeches.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'popit_url': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        'speeches.speech': {
            'Meta': {'object_name': 'Speech'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'blank': 'True'}),
            'celery_task_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['speeches.Speaker']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['speeches']