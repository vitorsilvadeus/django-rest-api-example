from django.test import TestCase
from performance.models import Performance
from django.urls import reverse

class TestAPIView(TestCase):

    def setUp(self):
        Performance.objects.create(
            date='2017-05-17',
            channel='adcolony',
            country='US',
            os='ios',
            impressions=13886,
            clicks=336,
            installs=60,
            spend=100.8,
            revenue=210.24,
        )
        Performance.objects.create(
            date='2017-05-17',
            channel='apple_search_ads',
            country='DE',
            os='ios',
            impressions=3180,
            clicks=118,
            installs=25,
            spend=50,
            revenue=20,
        )

    def test_get(self):
        url = reverse('performance')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
