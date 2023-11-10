from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import index, contact, about, policy, terms,  sign

urlpatterns = [
    path('',index, name='index'),
    path('items/', include('item.urls')),
    path('contact/', contact, name='contact'),
    path('About/', about, name='about'),
    path('Privacy Policy/', policy, name='policy'),
    path('signup/', sign ,name='sign'),
    path('Terms/', terms, name='terms'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
