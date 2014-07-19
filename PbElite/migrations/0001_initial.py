# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Login'
        db.create_table(u'PbElite_login', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=128, primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('salt', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'PbElite', ['Login'])

        # Adding model 'User'
        db.create_table(u'PbElite_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['PbElite.Login'], unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'PbElite', ['User'])

        # Adding model 'RaspberryPi'
        db.create_table(u'PbElite_raspberrypi', (
            ('serial_num', self.gf('django.db.models.fields.CharField')(max_length=64, primary_key=True)),
            ('username', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PbElite.User'])),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('operating_system', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('street_num', self.gf('django.db.models.fields.IntegerField')()),
            ('street_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'PbElite', ['RaspberryPi'])

        # Adding model 'Circuit'
        db.create_table(u'PbElite_circuit', (
            ('circuit_num', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_num', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PbElite.RaspberryPi'])),
            ('circuit_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('state', self.gf('django.db.models.fields.BinaryField')()),
        ))
        db.send_create_signal(u'PbElite', ['Circuit'])

        # Adding model 'Reading'
        db.create_table(u'PbElite_reading', (
            ('reading_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('circuit_num', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PbElite.Circuit'])),
            ('voltage', self.gf('django.db.models.fields.FloatField')()),
            ('current', self.gf('django.db.models.fields.FloatField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'PbElite', ['Reading'])


    def backwards(self, orm):
        # Deleting model 'Login'
        db.delete_table(u'PbElite_login')

        # Deleting model 'User'
        db.delete_table(u'PbElite_user')

        # Deleting model 'RaspberryPi'
        db.delete_table(u'PbElite_raspberrypi')

        # Deleting model 'Circuit'
        db.delete_table(u'PbElite_circuit')

        # Deleting model 'Reading'
        db.delete_table(u'PbElite_reading')


    models = {
        u'PbElite.circuit': {
            'Meta': {'object_name': 'Circuit'},
            'circuit_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'circuit_num': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'serial_num': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PbElite.RaspberryPi']"}),
            'state': ('django.db.models.fields.BinaryField', [], {})
        },
        u'PbElite.login': {
            'Meta': {'object_name': 'Login'},
            'password': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'})
        },
        u'PbElite.raspberrypi': {
            'Meta': {'object_name': 'RaspberryPi'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'operating_system': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'serial_num': ('django.db.models.fields.CharField', [], {'max_length': '64', 'primary_key': 'True'}),
            'street_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'street_num': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PbElite.User']"})
        },
        u'PbElite.reading': {
            'Meta': {'object_name': 'Reading'},
            'circuit_num': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PbElite.Circuit']"}),
            'current': ('django.db.models.fields.FloatField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'reading_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voltage': ('django.db.models.fields.FloatField', [], {})
        },
        u'PbElite.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'username': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['PbElite.Login']", 'unique': 'True'})
        }
    }

    complete_apps = ['PbElite']