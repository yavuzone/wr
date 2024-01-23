from django.test import TestCase
import ipdb


class RestrictedPageTest(TestCase):
    def setUp(self):
        pass

    def testLogin(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue("login" in response.url)
