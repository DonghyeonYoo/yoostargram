from django.conf.urls import url
from django.contrib import admin

from users.views import *
from yoostargram.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
]
