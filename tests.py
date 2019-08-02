from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.reverse import reverse


class UserApiTestCase(TestCase):
    """User Api"""

    def setUp(self):
        self.c = Client()
        self.normal_user = User.objects.create_user(
            username="test", password="p455w0rD", email="test@gmail.com"
        )
        self.superuser = User.objects.create_superuser(
            username="superuser", password="p455w0rD", email="superuser@gmail.com"

        )

    # def test_can_get_user_list(self):
    #     """Test List user"""
    #     url = reverse("user-"list)
    #     resp = self.c.get(url)
    #     assert resp.status_code == 200, \
    #         "Expect 200 OK. got:{}".format(resp.status_code)
    #     num_users = len(resp.json())
    #     assert num_users ==2
    #     assert False is True
    #
    # def test_get_user_returns_correct_fields(self):
    #     """Get User/PK return User detail"""
    #     assert False is True
    #
    # def test_cannot_create_user_if_not_logged_in(self):
    #     """POST user return 401"""
    #     assert False is True
    #
    # def test_0nly_reseller_can_create_user:
    #     """"Post return 403 unauthorizated if not superuser"""
    #     assert False is True
    #
    # def test_can_create_user_if_logged_in(self):
    #     assert False is True
    #
    # def tearDown(self):
    #     for user in User.objects.all():
    #         user.delete()
