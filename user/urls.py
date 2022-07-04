from django.urls import path
from .views import testToken, userRegister, retreave_user
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  # path('login/', views.userLogin),
  # path('logout/', views.userLogout),
  path('<int:pk>/', retreave_user, name='retreave_user'),
  path('register/', userRegister, name='custom_uesr_register'),
  path('check/', testToken, name='check_token'),
  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
