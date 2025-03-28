"""lets_quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path ,include
from quiz import views as quiz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
]

handler404 = quiz_views.error_404
handler500 = quiz_views.error_500


handler404 = 'quiz.views.error_404'
handler500 = 'quiz.views.error_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
