from django.test import TestCase
from .models import New, Category


class NewTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='test')
        New.objects.create(title='test', content='testText', categories=Category.objects.get(name='test'))

    def test_new(self):
        new = New.objects.get(title='test')
        self.assertEqual(new.categories.name, 'test')
        self.assertEqual(new.categories.content, 'testText')



class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='test 001')

    def test_category(self):
        category = Category.objects.get(name='test 001')
        self.assertEqual(category.name, 'test 001')

class testViews(TestCase):
    def setUp(self):
        Category.objects.create(name='test')
        New.objects.create(title='test', content='test', categories=Category.objects.get(name='test'))

    def test_hello(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)

    def test_all_categories(self):
        response = self.client.get('/category/all')
        self.assertEqual(response.status_code, 200)

    def test_category(self):
        response = self.client.get('/category/1')
        self.assertEqual(response.status_code, 200)

    def test_news_detail(self):
        response = self.client.get('/news/1')
        self.assertEqual(response.status_code, 200)
