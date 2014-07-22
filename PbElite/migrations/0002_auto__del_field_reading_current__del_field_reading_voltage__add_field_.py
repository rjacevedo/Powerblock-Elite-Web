# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Reading.current'
        db.delete_column(u'PbElite_reading', 'current')

        # Deleting field 'Reading.voltage'
        db.delete_column(u'PbElite_reading', 'voltage')

        # Adding field 'Reading.power'
        db.add_column(u'PbElite_reading', 'power',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Reading.current'
        raise RuntimeError("Cannot reverse this migration. 'Reading.current' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Reading.current'
        db.add_column(u'PbElite_reading', 'current',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Reading.voltage'
        raise RuntimeError("Cannot reverse this migration. 'Reading.voltage' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Reading.voltage'
        db.add_column(u'PbElite_reading', 'voltage',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)

        # Deleting field 'Reading.power'
        db.delete_column(u'PbElite_reading', 'power')


    models = {
        u'PbElite.circuit': {
            'Meta': {'object_name': 'Circuit'},
            'circuit_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'circuit_num': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raspberry_pi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PbElite.RaspberryPi']"}),
            'state': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'PbElite.login': {
            'Meta': {'object_name': 'Login'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'PbElite.raspberrypi': {
            'Meta': {'object_name': 'RaspberryPi'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'serial_num': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'street_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'street_num': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PbElite.User']"})
        },
        u'PbElite.reading': {
            'Meta': {'object_name': 'Reading'},
            'circuit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PbElite.Circuit']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'power': ('django.db.models.fields.FloatField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'PbElite.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'login': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['PbElite.Login']", 'unique': 'True'})
        }
    }

    complete_apps = ['PbElite']