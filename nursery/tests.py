from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from nursery.models import Fableseed, Flower, FableBranch

# Create your tests here.


class NurseryViewTests(TestCase):
    """
    A class of tests ensuring that the Nursery page loads successfully and displays all expected content.

    """

    def test_nursery_html_template(self):
        """
        Test that the nursery page loads successfully,
        uses the correct template, and contains expected text.
        Returns an HTTP 200 response.
        """
        response = self.client.get(reverse("nursery"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "nursery/nursery.html")
        self.assertContains(response, "Test content")


class NurseryModelTests(TestCase):
    """
    A class of tests to ensure that the nursery models work as expected.
    Tests Fableseeds and Fablebranches.

    Verifies that the instances are created correctly,
    their fields contain expected values, and their string representations behave
    as expected, including truncation.

    """

    def setUp(self):
        """
        Create initial test data for users, flowers, fableseeds and 
        fablebranches to use across tests.
        """
        self.user = User.objects.create_user(
            username="lucytest", password="testpassword")
        self.flower = Flower.objects.create(flower_name="Lily")
        self.seed = Fableseed.objects.create(
            flower_type=self.flower,
            title="My 1st Fableseed",
            body="Once upon a time...",
            approval_status=True,
            author=self.user,
            fablebuds_earnt=1
        )
        self.branch = FableBranch.objects.create(
            seed=self.seed,
            body="Story text goes here",
            author=self.user,
            fablebuds_cost=1
        )
        self.longbody = (
            "This is a really long string that should truncate because it is longer than 50 characters and I don't want to display anything that long."
        )

        self.long_branch = FableBranch.objects.create(
            seed=self.seed,
            body=self.longbody,
            author=self.user,
            fablebuds_cost=1
        )

    def test_fableseed_creation_and_str(self):
        """
        Test that a Fableseed instance is created with expected field values
          and that its string representation returns correctly.
        """
        self.assertEqual(self.seed.title, "My 1st Fableseed")
        self.assertTrue(self.seed.approval_status)
        self.assertEqual(self.seed.body, "Once upon a time...")
        self.assertEqual(self.seed.fablebuds_earnt, 1)
        self.assertEqual(str(self.seed), "My 1st Fableseed by lucytest")

    def test_fablebranch_creation_and_str(self):
        """
        Test that a Fablebranch instance is created with expected field values
        and that its string representation returns the full body and author.
        """
        self.assertEqual(self.branch.seed, self.seed)
        self.assertEqual(self.branch.body, "Story text goes here")
        self.assertEqual(self.branch.author, self.user)
        self.assertEqual(self.branch.fablebuds_cost, 1)
        self.assertEqual(str(self.branch), "Story text goes here by lucytest")

    def test_fablebranch_str_truncates_long_body_text(self):
        """
        Test that the string representation of a FableBranch with a long body 
        truncates at 50 characters, followed by ellipsis and author.
        """
        expected = f"{self.longbody[:50]}... by {self.user.username}"
        self.assertEqual(str(self.long_branch), expected)

    def test_fableseed_view_renders_correct_template_and_info(self):
        """
        Test that the nursery view loads correctly and provides the expected data.
        This test performs a GET request on the nursery url and verifies:
        - that the response code is 200; 
        - that the nursery/nursery.html template renders the page; 
        - that the context contains a variable named fableseed_list;
        - that the fableseed list creates the specific seed object created for the test.
        """
        response = self.client.get(reverse("nursery"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "nursery/nursery.html")
        self.assertIn("fableseed_list", response.context)
        self.assertIn(self.seed, response.context["fableseed_list"])
