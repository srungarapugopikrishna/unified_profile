# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# from .models import update_user_profile
from .models import Profile
from .models import UserProfile


admin.site.register(Profile)
admin.site.register(UserProfile)
