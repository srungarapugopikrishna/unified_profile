# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# from .models import update_user_profile
from .models import Profile
from .models import UserProfile
from .models import DBPediaPersonData
from .models import DBPediaPerson

admin.site.register(Profile)
admin.site.register(UserProfile)
admin.site.register(DBPediaPersonData)
admin.site.register(DBPediaPerson)
