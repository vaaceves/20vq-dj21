"""vitalquestions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from questions.views import logout, index_spa, index_eng, LoginUserViewSpa, LoginUserViewEng, topic_spa, topic_eng, \
    contact_eng, contact_spa, about_eng, about_spa, question_eng, question_spa, all_videos_eng, all_videos_spa, \
    SignUpUserViewEng, SignUpUserViewSpa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout, name='logout'),
    # English Views
    path('', index_eng, name='index_eng'),
    path('en/login/', LoginUserViewEng.as_view(), name='login_eng'),
    path('en/signup/', SignUpUserViewEng.as_view(), name='signup_eng'),
    path('en/<slug>/', topic_eng, name='topic_eng'),
    path('en/view/<slug>/', question_eng, name='question_eng'),
    path('en/contact', contact_eng, name='contact_eng'),
    path('en/about', about_eng, name='about_eng'),
    path('en/videos', all_videos_eng, name='all_videos_eng'),
    # Spanish Views
    path('es/', index_spa, name='index_spa'),
    path('es/login/', LoginUserViewSpa.as_view(), name='login_spa'),
    path('es/signup/', SignUpUserViewSpa.as_view(), name='signup_spa'),
    path('es/<slug>/', topic_spa, name='topic_spa'),
    path('es/view/<slug>/', question_spa, name='question_spa'),
    path('es/contact', contact_spa, name='contact_spa'),
    path('es/about', about_spa, name='about_spa'),
    path('es/videos', all_videos_spa, name='all_videos_spa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = '20 Vital Questions'
