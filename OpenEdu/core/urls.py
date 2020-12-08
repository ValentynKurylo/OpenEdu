from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

urlpatterns = [
]
urlpatterns = [
    path('mains/', views.core, name='core'),
    path('mains/detail/<int:id>', views.detail, name='detail'),
    url(r'^login/$', views.user_login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('lessons/', views.lessons, name='lessons'),
    path('lessons/lesson/<int:id>', views.lesson, name='lesson'),
    path('', views.redir, name='redir'),
    path('mains/profile', views.profile, name='profile'),
    path('schedule', views.schedule, name='schedule'),
    path('lessonst/lesson/<int:id>', views.lessont, name='lessont'),
    path('lessonst/lesson/add/<int:id>', views.addchapter, name='addchapter'),
    path('lessonst/lesson/delete/<int:id>', views.deletechapter, name='deletechapter'),
    path('lessonst/', views.lessonst, name='lessonst'),
    path('schedulet', views.schedulet, name='schedulet'),
    path('lessonst/lesson/editchapter/<int:id>', views.editchapter, name='editchapter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
