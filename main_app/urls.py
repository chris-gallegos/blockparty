from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('global/profile/create', views.ProfileCreate.as_view(), name='profile_create'),
    path('global/', views.global_index, name='global_index'),
    path('global/<int:post_id>/', views.global_post_detail, name='global_post_detail'),
    path('global/create/', views.GlobalPostCreate.as_view(), name='global_post_create'),
    path('global/<int:pk>/update/', views.GlobalPostUpdate.as_view(), name='global_post_update'),
    path('global/<int:pk>/delete/', views.GlobalPostDelete.as_view(), name='global_post_delete')
]
