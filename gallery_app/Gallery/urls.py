from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
url(r'^$',views.start,name='Start'),
url(r'^image/(\d+)',views.image,name='description'),
url(r'^search/',views.search_category,name='search_category'),
url(r'^location/',views.london,name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
