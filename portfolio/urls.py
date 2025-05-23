from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  # Define urlpatterns first!
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Direct root URL to the main app
]

# Now add static file handling AFTER urlpatterns is defined
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
