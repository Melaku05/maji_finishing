from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from msigana_ecommerce.admin_site import admin_site
from django.views.generic import TemplateView
from django.contrib.staticfiles.views import serve

# from django.contrib import admin

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('blog/', include('blog.urls')),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', include('contact.urls')),
    path("gallery/", include("gallery.urls")),
    path('accounts/', include('allauth.urls')),
    path('minerals/', views.minerals, name='minerals'),
    path('main_video/', include('main_video.urls')),
    path("video-gallery/", include("video_gallery.urls")),
]
# admin.site.site_header = 'Tanabeles Login'

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media setup

