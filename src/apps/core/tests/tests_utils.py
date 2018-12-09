from __future__ import unicode_literals
from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

from apps.core.tests.mixins import StatusCodeAssertsMixin


class TestApp(TestCase, StatusCodeAssertsMixin):
    url = str(reverse('home')).replace('-RU', '')

    def auth_user(self, user, password):
        url = reverse('accounts:login')
        data = {
            'email': user.email,
            'password': password,
        }
        response = self.client.post(url, data, follow=True)
        self.assert200(response)
        self.assertEqual(response.context['user'], user)

    def url_access(self, user, password, status_code):
        """

        :param user:
        :param status_code:
        """
        self.auth_user(user, password)
        response = self.client.get(self.url)
        self.assertStatusCode(status_code, response)

    def test_access_anonymous(self):
        """ """
        self.client.logout()
        response = self.client.get(self.url)
        self.assert302(response)