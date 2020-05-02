
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import auth_login, auth_logout


urlpatterns = [
    url(r'^user_profile/$', views.user_profile_input, name='user_profile'),
    url(r'^home$', views.home, name='home'),
    url(r'^home_new$', views.home_new, name='home_new'),
    url(r'^$', views.home, name='home'),
    path('profile/<username>', views.user_profile_display),
    path('profile/<username>/<platform>', views.user_profile_redirect),
    path('test', views.test),
    path('human_search', views.human_search),
    url(r'^dbpedia_to_app$', views.dbpedia_to_app),
    url(r'^dbpedia_to_app_person_data$', views.dbpedia_to_app_person_data),
    # path('<username>', views.test),
    url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'login.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup')
]