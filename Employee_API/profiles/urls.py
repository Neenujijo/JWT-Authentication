
from django.urls import path
from . import views


urlpatterns = [
    # path('login/',views.UserLoginView.as_view(),name='profile'),
    path('',views.ProfileCreateView.as_view(),name='profiles'),
    path('<int:profile_id>/',views.ProfileIdView.as_view(),name='profile_id'),
    path('designation/',views.UserDesignationView.as_view(),name='designation'),

    
]
