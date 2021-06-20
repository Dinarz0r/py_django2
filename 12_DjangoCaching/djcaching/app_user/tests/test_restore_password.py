from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from app_user.models import UserModel

USER_EMAIL = 'test@company.com'
OLD_PASSWORD = 'testpassword'


class RestorePasswordTest(TestCase):
    """Клас тестирования восстановления пароля"""
    def test_restore_password_url_exists_at_desired_location(self):
        """ Проверка на работу ссылки приложения /app_users/restore_password"""
        response = self.client.get(reverse('restore_password'))
        self.assertEqual(response.status_code, 200)

    def test_items_exist_at_desired_location(self):
        """ Тесты на вход по ссылке /app_goods/items/,
        а так же проверяем что используем шаблон 'goods/items_list.html' и то что вернул код 200"""
        response = self.client.get(reverse('restore_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/restore_password.html')

    def test_post_restore_password(self):
        """ тест на отправку письма на почту при пост запросе о восстановлении пароля"""
        user = User.objects.create(username='test', email=USER_EMAIL)
        response = self.client.post(reverse('restore_password'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 200)
        from django.core.mail import outbox
        self.assertEqual(len(outbox), 1)
        # этим кодом убедимся что в поле адресат будет находиться адрес эл. почты
        # лица который запросил восстановление пароля
        self.assertIn(USER_EMAIL, outbox[0].to)

    def test_if_password_was_changed(self):
        """ Тест на корректность работы формы на изменение пароля"""
        user = User.objects.create(username='test', email=USER_EMAIL, )
        user.set_password(OLD_PASSWORD)
        user.save()
        old_password_hash = user.password
        response = self.client.post(reverse('restore_password'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 200)
        user.refresh_from_db()
        self.assertNotEqual(old_password_hash, user.password)
