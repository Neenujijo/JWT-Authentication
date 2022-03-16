from django.urls import path
from . import views


urlpatterns = [
    # path('',views.HelloProfileView.as_view(),name='profile'),
    path('',views.ProfileCreateView.as_view(),name='profiles'),
    path('profile/<int:profile_id>/',views.ProfileIdView.as_view(),name='profile_id'),
    # path('user/<int:user_id>/profiles',views.UserProfileView.as_view(),name='users_profile'),
    # path('user/<int:user_id>/profile/<int:profile_id>/',views.UserProfileDetailView.as_view(),name='user_profile_detail'),

]
