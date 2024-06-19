from django.urls import path
from . import views
from .views import MyTokenObtainPairView, RegisterView, getRoutes, testEndPoint, get_profile, update_profile,get_profiles
# from .views import CrudViewset

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('routes/', getRoutes, name='routes'),
    # path('profile/', get_profile, name='get_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
    # crud
    path('profiles/', get_profiles, name='get_profiles'),
    # path('crud_app/<int:id>', CrudViewset.as_view())
]


# from rest_framework_simplejwt.views import TokenRefreshView
# from django.urls import path
# from api import views

# urlpatterns = [
#     path("token/", views.MyTokenObtainPairView.as_view()),
#     path("token/refresh/", TokenRefreshView.as_view()),
#     path("register/", views.RegisterView.as_view()),
#     path("dashboard/", views.dashboard),
# #     path('token/refresh/', TokenRefreshView.as_view(),
# # name='token_refresh'),
# ]