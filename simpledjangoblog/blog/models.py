from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
	username = models.CharField(max_length=70)

	def __str__(self):
		return self.username

class Post(models.Model):
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
    	return self.headline

    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)