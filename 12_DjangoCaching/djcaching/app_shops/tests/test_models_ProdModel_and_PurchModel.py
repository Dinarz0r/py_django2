from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from app_shops.models import ProductsModel, ShopsModel, PurchaseHistoryModel

COUNT_NEW_SHOP = 10
USERNAME = 'testuser'
USER_PASSWORD = 'Qq12345678!'


class ProductsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Создаем Юзера, и 10 магазинов от имени созданного юзера.
        """
        cls.user = User.objects.create_user(USERNAME, 'admin@test.com', USER_PASSWORD)
        for shop_index in range(1, COUNT_NEW_SHOP + 1):
            ShopsModel.objects.create(
                name_shop=f'Магазин {shop_index}',
                telephone=f'+796534716{shop_index}'
            )
        """создаем 10 товаров"""
        for shop_index in range(1, 1 + COUNT_NEW_SHOP):
            ProductsModel.objects.create(
                product=f'Товар {shop_index}',
                price=shop_index,
                article=f'{shop_index}',
                shop_id=f'{shop_index}'
            )

        """создаем 10 покупок и записываем в базу."""
        for i_product in range(1, COUNT_NEW_SHOP + 1):
            PurchaseHistoryModel.objects.create(
                user_id=cls.user.id,
                goods_id=i_product,
                price=10000 + i_product,

            )

    def test_products_number(self):
        """
        Тут проверяем заполненную базу Товаров в кол-ве COUNT_NEW_SHOP записей!
        """
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        self.assertTrue(ProductsModel.objects.all().count() == COUNT_NEW_SHOP)

    def test_purchase_hist_count(self):
        """
        Тут проверяем заполненную базу истории покупок в кол-ве COUNT_NEW_SHOP записей!
        """
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        self.assertTrue(PurchaseHistoryModel.objects.all().count() == COUNT_NEW_SHOP)

    def test_detail_product_page(self):
        """ Тест проверки детальной страницы товара. Проверяем созданные 10 товаров.
        Проверяем 11-ый товар которого нет на вызов исключения,
        на присутствие текста на странице 'ТОВАР'"""
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        for i_product in range(len(PurchaseHistoryModel.objects.all())):
            response = self.client.get(f'/shop/buy/{i_product + 1}')
            # self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'shops/detail_product_page.html')
            self.assertContains(response, 'ТОВАР')
        response = self.client.get(f'/shop/buy/11')
        self.assertNotEqual(response.status_code, 200)
