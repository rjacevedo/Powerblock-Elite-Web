from . import models
from django.utils.timezone import utc
import factory
import datetime

class LoginFactory(factory.Factory):
	class Meta:
		model = models.Login

	username = factory.Sequence(lambda n: 'user%d' % n)
	password = "password"
	salt = "salt"

class UserFactory(factory.Factory):
	class Meta:
		model = models.User

	username = factory.SubFactory(LoginFactory)
	first_name = "John"
	last_name = "Doe"
	email = factory.LazyAttribute(
		lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name).lower())

class RaspberryPiFactory(factory.Factory):
	class Meta:
		model = models.RaspberryPiFactory

	serial_num = factory.Sequence(lambda n: "%s%s".format(n, factory.fuzzy.FuzzyText()))
	login = factory.SubFactory(UserFactory)
	model = "random_model"
	operating_system = "linux"
	street_num = 123
	street_name = "Fake st."
	city = "Fakilton"
	province = "ON"
	postal_code ="N2L4G3"

class CircuitFactory(models.Factory):
	class Meta:
		model = models.Circuit

	circuit_num = 2
	serial_num = factory.SubFactory(RaspberryPiFactory)
	circuit_name = "Room"
	state = 0

class ReadingFactory(models.Factory):
	class Meta:
		model = models.Reading

	circuit_num = factory.SubFactory(CircuitFactory)
	voltage = factory.fuzzy.FuzzyInteger(0,25)
	current = factory.fuzzy.FuzzyInteger(0,30)
	datetime = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=utc))
