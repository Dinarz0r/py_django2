from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

USER_EMAIL = 'test@company.com'


class LoginUserTest(TestCase):
    """Класс тестирования процессов связанных с логированием
    в том числе тестирования работы страниц"""
    @classmethod
    def setUpTestData(cls):
        cls.USERNAME = 'testusername'
        cls.PASSWORD = 'Qq12345678!'
        cls.user = User.objects.create_user(username=cls.USERNAME, email=USER_EMAIL, password=cls.PASSWORD)

    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/reg_page.html')

    def test_login(self):
        """Тест логирования созданного аккаунта"""
        form = {'username': self.USERNAME, 'password': self.PASSWORD}
        response = self.client.post(reverse('login'), form)
        self.assertRedirects(response, reverse('main_page'))

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('main_page'))
