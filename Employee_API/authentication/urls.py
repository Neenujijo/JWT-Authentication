from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
# from authentication.views import logout_view

urlpatterns = [
    path('signup/',views.UserCreateView.as_view(),name='sign_up'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/',views.UserLogoutView.as_view(), name='logout'),

    path('',views.UserView.as_view(),name='employee_list'),
    path('<int:user_id>/',views.UserEditView.as_view(),name='user_id'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
]