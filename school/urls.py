from django.urls import path

from .views import ClassroomAPIView, ClassroomAPIViewStaff, HelloView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('', ClassroomAPIView.as_view()),
    path('create/', ClassroomAPIViewStaff.as_view()),
    path('login/', ObtainAuthToken.as_view()),
    path('hello/', HelloView)
    # path('login-token/', obtain_auth_token()),
]
