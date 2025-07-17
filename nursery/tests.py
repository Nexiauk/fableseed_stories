from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from nursery.models import Fableseed, Flower

# Create your tests here.
class NurseryViewTests(TestCase):
    """
    A class of tests ensuring that the Nursery page loads successfully and displays all expected content.

    """
    def test_nursery_html_template(self):
        """Test that the nursery page loads successfully,
        uses the correct template, and contains expected text.
        Returns an HTTP 200 response.
        """
        response = self.client.get(reverse("nursery"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "nursery/nursery.html")
        self.assertContains(response, "Test content")

class NurseryModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="lucytest", password="testpassword")
        self.flower = Flower.objects.create(flower_name="Lily")

    def test_fableseed_creation_and_str(self):
        fableseed = Fableseed.objects.create(
            flower_type=self.flower,
            title="My 1st Fableseed",
            body="Once upon a time...",
            approval_status=True,
            author=self.user,
            fablebuds_earnt=1,
        )

        self.assertEqual(fableseed.title, "My 1st Fableseed")
        self.assertTrue(fableseed.approval_status)
        self.assertEqual(fableseed.body, "Once upon a time...")
        self.assertEqual(fableseed.fablebuds_earnt, 1)

        self.assertEqual(str(fableseed), "My 1st Fableseed by lucytest")