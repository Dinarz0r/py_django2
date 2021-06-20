from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class EditUserNameTest(TestCase):
    """ Класс тестирования редактирования информации аккаунта"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='EditName',
            first_name='Иван',
            last_name='Иванов',
            email='email@ggwp.com',
            password='test1234!'
        )

    def test_edit_account(self):
        """Тест внесения изменений в модель User с последующей проверкой
        на self.assertNotEqual нового и старого имени"""
        self.client.login(username='EditName', password='test1234!')
        old_first_name = self.user.first_name
        NEW_NAME = 'Новое имя'
        form = {'last_name': NEW_NAME, 'first_name': 'Новая фамилия'}
        self.client.post(reverse('edit_account'), form)
        self.user.refresh_from_db()
        self.assertNotEqual(old_first_name, self.user.first_name)
