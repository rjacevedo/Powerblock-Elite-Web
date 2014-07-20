from django.test import TestCase
from .. import models
from ..factories import factories

class FactoryTestCase(TestCase):
    def setUp(self):
   		self.user = factories.UserFactory.build()
   		self.circuit = factories.CircuitFactory.build()
   		self.reading = factories.ReadingFactory.build()
   		self.rpi = factories.RaspberryPiFactory.build()
   		self.login = factories.LoginFactory.build()

    def test_factories_build_correctly(self):
        self.assertIsInstance(self.user, models.User)
        self.assertIsInstance(self.circuit, models.Circuit)
        self.assertIsInstance(self.reading, models.Reading)
        self.assertIsInstance(self.rpi, models.RaspberryPi)
        self.assertIsInstance(self.login, models.Login)        
