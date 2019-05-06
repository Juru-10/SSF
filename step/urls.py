from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^admin/$',views.admin,name='admin'),
    url(r'^school/$',views.school,name='school'),
    url(r'^add_guide/',views.add_guide,name='add_guide'),
    url(r'^add_student/$',views.add_student,name='add_student'),
    url(r'^add_level/$',views.add_level,name='add_level'),
    url(r'^student/$',views.student,name='student'),
    url(r'^add_marks/(\d+)/(\d+)/',views.add_marks,name='add_marks'),
    url(r'^add_discipline/(\d+)/(\d+)/',views.add_discipline,name='add_discipline'),
    url(r'^levels/(?P<id>[0-9999]+)/$',views.levels,name='levels'),
    url(r'^school_login/$',views.school_login,name='school_login'),
    url(r'^student_login/$',views.student_login,name='student_login'),
    url(r'^guide_login/$',views.guide_login,name='guide_login'),
    url(r'^guides/$',views.guides,name='guides'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
