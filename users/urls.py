from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),  # post-회원가입
    path('auth/', views.UserAuthView.as_view(),name='user_view'),  # post-로그인/delete-로그아웃/get-유저확인
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 토큰?
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 토큰 재발급?
]
