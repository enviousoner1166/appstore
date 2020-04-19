from django.db import models

# Create your models here.


class App(models.Model):
    '''
    Represents an application to be submitted to the store
    '''
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    mini_description = models.CharField(max_length=120)
    description = models.TextField(max_length=300)
    copyright = models.CharField(max_length=120)
    publisher = models.ForeignKey(
        'Publisher', on_delete=models.CASCADE, related_name='apps')
    categories = models.ManyToManyField('Category')


class Publisher(models.Model):
    '''
    Represents a publisher of an app. Publisher can publish
    many apps
    '''
    name = models.CharField(max_length=100, help_text='Name of publisher')
    website = models.URLField(help_text='Official website of app')
    support_url = models.URLField(help_text='Link to useful app resources')
    privacy_policy_url = models.URLField(help_text='Privacy policy link')


class Category(models.Model):
    '''
    Represents variaous app categories
    '''
    name = models.CharField(max_length=100, help_text='Category name')
    description = models.TextField(
        max_length=200, help_text='Category description')

