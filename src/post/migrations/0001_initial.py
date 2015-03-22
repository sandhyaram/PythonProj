# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'post_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default='')),
            ('image', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('article', self.gf('django.db.models.fields.TextField')(max_length=15000, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        ))
        db.send_create_signal(u'post', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'post_post')


    models = {
        u'post.post': {
            'Meta': {'object_name': 'Post'},
            'article': ('django.db.models.fields.TextField', [], {'max_length': '15000', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        }
    }

    complete_apps = ['post']