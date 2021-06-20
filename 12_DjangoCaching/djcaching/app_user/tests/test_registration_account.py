from django.test import TestCase
from django.urls import reverse


class RegistrationUserTest(TestCase):
    """Класс тестирования бизнес-логики относящейся
    регистрации пользователя и страницы"""
    def test_registration_page(self):
        """Тест страницы регистрации"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/reg_page.html')

    def test_completion_register_form_and_login(self):
        """Заполняем форму регистрации """
        form = {
            'username': 'NewUserTest',
            'first_name': 'ТестИмя',
            'last_name': 'ТестФамилия',
            'email': 'testemail@company.ru',
            'city': 'New York',
            'telephone': '79653479595',
            'balance': 33000.00,
            'password1': 'Qq1234567890!',
            'password2': 'Qq1234567890!',
        }
        response = self.client.post(reverse('register'), form)
        self.assertRedirects(response, reverse('main_shops_page'))

        """ Логаут """
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('main_shops_page'))

        """ Далее логинимся под зарегинеными данными"""

        response = self.client.post(reverse('login'), {
            'username': 'NewUserTest',
            'password': 'Qq1234567890!',
        })
        self.assertRedirects(response, reverse('main_shops_page'))
