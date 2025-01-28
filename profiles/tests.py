from django.test import TestCase
from django.contrib.auth.models import User
from .models import User_Profile, User_Library, Game, Platform, Privacy


class UserProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.privacy = Privacy.objects.create(privacy='Public')
        self.game = Game.objects.create(game='Test Game')
        self.platform = Platform.objects.create(platform='Test Platform')
        self.user_profile = User_Profile.objects.create(
            user=self.user,
            game=self.game,
            platform=self.platform,
            privacy=self.privacy
        )

    def test_user_profile_creation(self):
        self.assertTrue(isinstance(self.user_profile, User_Profile))
        self.assertEqual(self.user_profile.__str__(), self.user.username)

    def test_user_profile_relationships(self):
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.game, self.game)
        self.assertEqual(self.user_profile.platform, self.platform)
        self.assertEqual(self.user_profile.privacy, self.privacy)


class UserLibraryModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.game = Game.objects.create(game='Test Game')
        self.user_library = User_Library.objects.create(
            user=self.user,
            game=self.game
        )
        self.user_library.platform.set(
            [Platform.objects.create(platform='Test Platform')])

    def test_user_library_creation(self):
        self.assertTrue(isinstance(self.user_library, User_Library))
        self.assertEqual(self.user_library.__str__(), self.user.username)

    def test_user_library_relationships(self):
        self.assertEqual(self.user_library.user, self.user)
        self.assertEqual(self.user_library.game, self.game)
        self.assertEqual(list(self.user_library.platform.all()), [
                         Platform.objects.get(platform='Test Platform')])
