from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^(?P<testFuncName>[^\/]+)$", views.index),
    re_path(r"^$", views.index),
]
# ]  + static(settings.STATIC_URL, document_root='/Users/wtchen/Research/anaforaFileDevelop/anaforaProjectFile/')
