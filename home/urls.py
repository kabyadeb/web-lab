from  django.urls import path
from . import views

urlpatterns = [
   path('',views.HomeViewAll.as_view(),name=''),
   path('blogs/',views.HomeViewBlogs.as_view(),name='blogs'),
   path('create/',views.Createblog,name='create'),
   path('place/<int:pk>/', views.PlaceDetailView.as_view(), name='place_detail'),
   path('update/<int:pk>/',views.Updateblog.as_view(),name='update'),
   path('delete/<int:pk>/',views.Deleteblog.as_view(),name='delete'),
]