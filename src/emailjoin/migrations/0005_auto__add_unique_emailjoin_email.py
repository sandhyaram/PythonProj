# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'EmailJoin', fields ['email']
        db.create_unique(u'emailjoin_emailjoin', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'EmailJoin', fields ['email']
        db.delete_unique(u'emailjoin_emailjoin', ['email'])


    models = {
        u'emailjoin.emailjoin': {
            'Meta': {'object_name': 'EmailJoin'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC '", 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['emailjoin']