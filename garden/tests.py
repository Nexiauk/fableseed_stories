from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.

class UserProfileTests(TestCase):
    """
    Tests that the extended user profile fields are setup correctly when a
    UserProfile is created.
    """

    def setUp(self):
        """
        Create initial test data for a user
        """
        self.user = User.objects.create_user(
            username="lucytest",
            password="testpassword"
        )

    def test_user_profile_fields(self):
        """
        Test that the receiver signal creates or updates a UserProfile
        when a User instance is saved.

        Asserts that:
        - a UserProfile exists for the user
        - UserProfile.display_name is equal to the User's username
        - UserProfile.bio has defaults to the string "Hi"
        - UserProfile.profile_picture is set(truthy)
        - UserProfile.fablebuds_count defaults to 0
        """
        self.assertTrue(self.user.userprofile)
        self.assertEqual(self.user.userprofile.display_name, "lucytest")
        self.assertEqual(self.user.userprofile.bio, "Hi")
        self.assertTrue(self.user.userprofile.profile_picture)
        self.assertEqual(self.user.userprofile.fablebuds_count, 0)
