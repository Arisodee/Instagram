from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from instagram import views as user_views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^update_profile/', user_views.update_profile,name = 'update_profile'),
    url(r'^accounts/register/', views.register, name='register'),
    url(r'^new_post/', views.new_post,name ='new_post'),
]
 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)