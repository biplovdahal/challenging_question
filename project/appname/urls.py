from django.conf.urls import url
from rest_framework import routers
from project.appname.views import  Members
from rest_framework_swagger.views import get_swagger_view
 
router = routers.DefaultRouter()

schema_view = get_swagger_view(title='Instawork API')

urlpatterns = [
    url(r'members', Members.as_view()),
    url(r'^docs/', schema_view),
]
 
urlpatterns += router.urls