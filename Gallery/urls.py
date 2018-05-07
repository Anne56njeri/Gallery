from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
url(r'^$',views.start,name='Start'),
url(r'^image/(\d+)',views.image,name='description'),
url(r'^search/',views.search_category,name='search_category'),
url(r'^London/',views.london,name='location'),
url(r'^China/',views.china,name='location1'),
url(r'^Malawi/',views.malawi,name='location2'),
url(r'^Europe/',views.europe,name='location3'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
