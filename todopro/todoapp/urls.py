from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('detail',views.detail,name='detail')
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvedit/<int:pk>/',views.Taskupdateview.as_view(),name='cbvedit'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete'),



]
