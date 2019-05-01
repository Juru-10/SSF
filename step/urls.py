from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/$',views.admin,name='admin'),
    url(r'^school/$',views.school,name='school'),
    url(r'^add_guide/$',views.add_guide,name='add_guide'),
    url(r'^add_student/$',views.add_student,name='add_student'),
    url(r'^add_level/$',views.add_level,name='add_level'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
