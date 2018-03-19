from django.conf.urls import url
from rest_framework import routers
from project.appname.views import  Members
from rest_framework_swagger.views import get_swagger_view
 
router = routers.DefaultRouter()

schema_view = get_swagger_view(title='Instawork API')

urlpatterns = [
    url(r'^docs/', schema_view),
]
router.register(r'members', Members)
 
urlpatterns += router.urls