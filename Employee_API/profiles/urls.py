from xml.etree.ElementInclude import include
from django.urls import path
from . import views


urlpatterns = [
    # path('',views.HelloProfileView.as_view(),name='profile'),
    path('',views.ProfileCreateView.as_view(),name='profiles'),
    path('profile/<int:profile_id>/',views.ProfileIdView.as_view(),name='profile_id'),
    
]
