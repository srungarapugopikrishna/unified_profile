# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class UserProfile(models.Model):
    name = models.CharField(max_length=100, null=False)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email = models.EmailField(null=False)
    facebook = models.URLField(null=False)
    instagram = models.URLField(null=False)
    twitter = models.URLField(null=False)
    github = models.URLField(null=False)
    stackoverflow = models.URLField(null=False)
    resume = models.URLField(null=False)
    hackerrank = models.URLField(null=False)
    hackerearth = models.URLField(null=False)
    others = models.URLField(null=False)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
