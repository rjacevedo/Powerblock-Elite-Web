# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Schedule'
        db.create_table(u'PbElite_schedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('raspberry_pi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PbElite.RaspberryPi'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('circuit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PbElite.Circuit'])),
            ('state', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'PbElite', ['Schedule'])

        # Deleting field 'Circuit.circuit_num'
        db.delete_column(u'PbElite_circuit', 'circuit_num')

        # Adding field 'Circuit.changed'
        db.add_column(u'PbElite_circuit', 'changed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Schedule'
        db.delete_table(u'PbElite_schedule')


        # User chose to not deal with backwards NULL issues for 'Circuit.circuit_num'
        raise RuntimeError("Cannot reverse this migration. 'Circuit.circuit_num' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Circuit.circuit_num'
        db.add_column(u'PbElite_circuit', 'circuit_num',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)

        # Deleting field 'Circuit.changed'
        db.delete_column(u'PbElite_circuit', 'changed')


    models = {
        u'PbElite.circuit': {
            'Meta': {'object_name': 'Circuit'},
            'changed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'circuit_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
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
        u'PbElite.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'circuit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PbElite.Circuit']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raspberry_pi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PbElite.RaspberryPi']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'state': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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