from django.test import TestCase

from .models import App, Publisher, Category

# Create your tests here.


class AppModelTest(TestCase):

    def setUp(self):
        # create model

        publisher = Publisher.objects.create(
            name='Pusbliser',
            website='www.publisher.co',
            support_url='www.help.publisher.co',
            privacy_policy_url='www.publisher/policies',
        )

        categories = [
            {
                'name': 'Art',
                'description': 'Applications relating to art culture'
            },
            {
                'name': 'Education',
                'description': 'Education related apps'
            }
        ]

        saved_categories = []

        for item in categories:
            saved_categories.append(Category.objects.create(
                name=item['name'],
                description=item['description']
                ))

        app = App.objects.create(
            name='Test App',
            version='0.0.1',
            mini_description='''Cras in scelerisque tortor. Duis bibendum
             justo tempor ultrices sodales''',
            description='''
            Vestibulum massa nisl, condimentum placerat
            ipsum quis, auctor malesuada velit. Donec eget
             augue et nunc ultrices sagittis. Orci varius
             natoque penatibus et magnis dis parturient montes,
             nascetur ridiculus mus. Donec et rutrum elit.
             Cras in scelerisque tortor. Duis bibendum
             justo tempor ultrices sodales.
            ''',
            copyright='© 2020 Publisher Inc',
            publisher=publisher,
        )

        for item in saved_categories:
            app.categories.add(item)

    def test_app_create(self):
        self.assertEquals(App.objects.count(), 1)
