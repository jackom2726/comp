from __future__ import unicode_literals

from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = models.TextField()
    def show(self):
    	print '\n{0} \n{1} \nBy {2} \n{3} \n\n {4}\n'.format(self.title, self.subtitle, self.contributors, self.pub_date, self.text)


class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    def die(self):
    	Model.delete(using=DEFAULT_DB_ALIAS, keep_parents=False)

# Create your models here.


