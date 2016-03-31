from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from users.views import *
from yoostargram.views import *
from posts.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^posts/$', PostListView.as_view(), name='posts'),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post'),
    url(r'^posts/(?P<pk>\d+)/comments/$', post_comments, name='post-comments'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^(?P<slug>\w+)/$', ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
