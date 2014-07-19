from django.utils.timezone import utc
from .. import models
import factory
import factory.fuzzy
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

    login = factory.SubFactory(LoginFactory)
    first_name = "John"
    last_name = "Doe"
    email = factory.LazyAttribute(
        lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name).lower())

class RaspberryPiFactory(factory.Factory):
    class Meta:
        model = models.RaspberryPi

    serial_num = factory.Sequence(lambda n: "%s%s".format(n, factory.fuzzy.FuzzyText()))
    user = factory.SubFactory(UserFactory)
    model = "random_model"
    street_num = 123
    street_name = "Fake st."
    city = "Fakilton"
    country = "Canada"
    postal_code ="N2L4G3"

class CircuitFactory(factory.Factory):
    class Meta:
        model = models.Circuit

    circuit_num = 2
    raspberry_pi = factory.SubFactory(RaspberryPiFactory)
    circuit_name = "Room"
    state = 0

class ReadingFactory(factory.Factory):
    class Meta:
        model = models.Reading

    circuit = factory.SubFactory(CircuitFactory)
    voltage = factory.fuzzy.FuzzyInteger(0,25)
    current = factory.fuzzy.FuzzyInteger(0,30)
    timestamp = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=utc))
