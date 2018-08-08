from customers.views import TenantView
from django.conf.urls import url


urlpatterns = [
     url(r'^(?P<db>\w+)/$', TenantView.as_view()),
]