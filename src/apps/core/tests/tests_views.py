# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from apps.core.tests.tests_utils import TestApp
from django.urls import reverse


class TestHome(TestApp):
    """ Тестирование .. """

    def setUp(self):
        """ Авторизация пользователя """
        super(TestHome, self).setUp()
        self.url = reverse('home')

    def tearDown(self):
        """ Очистка после каждого метода """
        super(TestHome, self).tearDown()
        self.client.logout()

    def test_view_url(self):
        """ Проверка URL адреса и используемого шаблона """
        response = self.client.get(self.url)
        self.assert200(response)
