from django.test import TestCase
from catalog.models import Country


class CountryTestCase(TestCase):
    fixtures = ['catalog/tests/fixtures/countries.json']

    def test_str_representation(self):
        country = Country.objects.get(id=1)
        self.assertEqual(country.name, str(country))
