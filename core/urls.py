from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,re_path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', index, name='index'),
    path('feature/', feature, name='feature'),
    path('appointment/', appointment, name='appointment'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
]


urlpatterns += static(settings.STATIC_URL, 
                      document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                       document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r"^.,*",page_404)]
