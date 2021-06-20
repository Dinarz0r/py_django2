from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_blog.models import Blog

COUNT_NEW_BLOG = 10
USERNAME = 'testuser'
USER_PASSWORD = 'Qq12345678!'


class MainPageTest(TestCase):
    """Проверяем главную страницу """

    def test_main_page(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/main_list.html')
        self.assertContains(response, 'SkillBLOG')


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Создаем Юзера, и 10 блогов от имени созданного юзера.
        """
        cls.user = User.objects.create_user(USERNAME, 'admin@test.com', USER_PASSWORD)
        for blog_index in range(COUNT_NEW_BLOG):
            Blog.objects.create(
                title=f'Блог test {blog_index}',
                text=f'Test blog {blog_index}',
                user_id=cls.user.id,
            )

    def test_page_add_blog(self):
        """Тестируем страницу создания блога проверяем ссылку, возврат 200 кода и используемый шаблон"""
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        response = self.client.get(reverse('add_blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/new_blog.html')

    def test_blog_number(self):
        """
        Тут проверяем заполненную базу Блогов в кол-ве COUNT_NEW_BLOG записей!
        """
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        self.assertTrue(Blog.objects.all().count() == COUNT_NEW_BLOG)

    def test_detail_page(self):
        """ Тест проверки детальной страницы. Проверяем созданные 10 блогов.
        Проверяем 11-ый блог которого нет на вызов исключения,
        на присутствие текста на странице 'Дата публикации'"""
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        for i_blog in range(len(Blog.objects.all())):
            response = self.client.get(f'/blog/{i_blog + 1}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'blog/detail_blog.html')
            self.assertContains(response, 'Дата публикации')
        response = self.client.get(f'/blog/11')
        self.assertNotEqual(response.status_code, 200)

    def test_add_csv_blog_page(self):
        """ Тес работы страницы массовой загрузки блогов с использованием CSV"""
        self.client.login(username=self.user.username, password=USER_PASSWORD)
        response = self.client.get(reverse('add_csv_blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_csv_blog.html')
        self.assertContains(response, 'Массовая загрузка блогов CSV')
