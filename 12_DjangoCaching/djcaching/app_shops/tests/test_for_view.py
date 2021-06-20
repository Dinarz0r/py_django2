from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from app_shops.models import ShopsModel, PurchaseHistoryModel

COUNT_NEW_SHOP = 10
USERNAME = 'testuser'
USER_PASSWORD = 'Qq12345678!'


class MainPageTest(TestCase):
    """Проверяем главную страницу """

    def test_main_page(self):
        response = self.client.get(reverse('main_shops_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/main_page_list_shop.html')
        self.assertContains(response, 'Список магазинов')


class ShopModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Создаем Юзера, и 10 магазинов от имени созданного юзера.
        """
        cls.user = User.objects.create_user(USERNAME, 'admin@test.com', USER_PASSWORD)
        for shop_index in range(COUNT_NEW_SHOP):
            ShopsModel.objects.create(
                name_shop=f'Магазин {shop_index}',
                telephone=f'+796534716{shop_index}'
            )

    def test_shop_number(self):
        """
        Тут проверяем заполненную базу Магазинов в кол-ве COUNT_NEW_BLOG записей!
        """
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        self.assertTrue(ShopsModel.objects.all().count() == COUNT_NEW_SHOP)

    def test_detail_page(self):
        """ Тест проверки детальной страницы. Проверяем созданные 10 детальных страниц магащинов.
        Проверяем 11-ый магазин которого нет на вызов исключения,
        на присутствие текста на странице 'Магазин'"""
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        for i_shop in range(len(ShopsModel.objects.all())):
            response = self.client.get(f'/shop/{i_shop + 1}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'shops/detail_shop_page.html')
            self.assertContains(response, 'Магазин ')
        response = self.client.get(f'/shop/11')
        self.assertNotEqual(response.status_code, 200)
