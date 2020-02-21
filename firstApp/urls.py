from django.urls import path, include
from . import views
from .views import Another

urlpatterns = [
    path('firstFunctionView', views.first),
    path('firstClassView', Another.as_view()),
    path('firstTemplate', views.firstTemplate),
    path('dynamicTemplate', views.dynamicTemplate)
]
