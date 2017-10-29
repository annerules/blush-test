from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
]

urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)
