from django.test import TestCase
from django.urls import reverse

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