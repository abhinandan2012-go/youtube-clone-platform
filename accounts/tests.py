from django.test import TestCase


class AccountsViewsTests(TestCase):
    def test_signup_page_renders(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
