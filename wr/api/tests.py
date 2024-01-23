from django.test import TestCase
from django.contrib.auth import get_user_model
import ipdb


class ApiTokenTest(TestCase):
    def setUp(self):
        self.email = "admin@webrunners.de"
        self.password = "admin"
        user = get_user_model().objects.create(email=self.email)
        user.set_password(self.password)
        user.save()

    def testAuthentication(self):
        response = self.client.post(
            "/api/User/GetToken", {"email": self.email, "password": self.password}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

        response = self.client.get(
            f"/api/User/ValidateToken?token={response.json()['access']}"
        )

        self.assertEqual(response.status_code, 200)
