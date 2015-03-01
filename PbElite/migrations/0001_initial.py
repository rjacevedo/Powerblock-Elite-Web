# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Login'
        db.create_table(u'PbElite_login', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('salt', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'PbElite', ['Login'])

        # Adding model 'User'
        db.create_table(u'PbElite_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('login', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['PbElite.Login'], unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'PbElite', ['User'])

        # Adding model 'RaspberryPi'
        db.create_table(u'PbElite_raspberrypi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_num', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PbElite.User'])),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('street_num', self.gf('django.db.models.fields.IntegerField')()),
            ('street_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'PbElite', ['RaspberryPi'])

        # Adding model 'Circuit'
        db.create_table(u'PbElite_circuit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('raspberry_pi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PbElite.RaspberryPi'])),
            ('circuit_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('state', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('changed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'PbElite', ['Circuit'])

        # Adding model 'Reading'
        db.create_table(u'PbElite_reading', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('circuit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PbElite.Circuit'])),
            ('power', self.gf('django.db.models.fields.FloatField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'PbElite', ['Reading'])

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

        # Adding model 'UserSessions'
        db.create_table(u'PbElite_usersessions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PbElite.User'])),
            ('randomhash', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('expiry_datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'PbElite', ['UserSessions'])


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

        # Deleting model 'Schedule'
        db.delete_table(u'PbElite_schedule')

        # Deleting model 'UserSessions'
        db.delete_table(u'PbElite_usersessions')


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
        },
        u'PbElite.usersessions': {
            'Meta': {'object_name': 'UserSessions'},
            'expiry_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'randomhash': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PbElite.User']"})
        }
    }

    complete_apps = ['PbElite']