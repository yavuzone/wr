from django.test import TestCase
from django.contrib.auth import get_user_model
import ipdb


class ApiTokenTest(TestCase):
    def setUp(self):
        self.email = "admin@webrunners.de"
        self.password = "admin"
        self.user = get_user_model().objects.create(email=self.email)
        self.user.set_password(self.password)
        self.user.save()

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

    def testCRUD(self):
        response = self.client.post(
            "/api/User/GetToken", {"email": self.email, "password": self.password}
        )
        token = response.json()["access"]
        self.client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        response = self.client.post(
            "/api/Admin/UserManagement", {"email": "onur@onur.de", "password": 1234}
        )
        self.assertTrue("You do not have permission" in str(response.content))

        self.user.is_superuser = True
        self.user.save()
        response = self.client.post(
            "/api/Admin/UserManagement", {"email": "onur@onur.de", "password": 1234}
        )
        self.assertEqual(response.status_code, 200)
        user_id = response.json()["user_id"]

        response = self.client.put(
            f"/api/Admin/UserManagement/{user_id}",
            {"email": "onu2r@onur.de", "password": "123456"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["email"], "onu2r@onur.de")

        response = self.client.delete(
            f"/api/Admin/UserManagement/{user_id}",
        )

        response = self.client.get(
            f"/api/Admin/UserManagement",
        )

        filtered_users = any(filter(lambda x: x["id"] == user_id, response.json()))

        self.assertFalse(filtered_users)
