from django.urls import path

from .views import home,updatemark,delete,addtask,update

urlpatterns=[
    path('',home,name='home'),
    path('updatemark<int:pk>',updatemark,name='updatemark'),
    path('delete<int:pk>',delete,name='delete'),
    path('addtask',addtask,name='addtask'),
    path('update<int:pk>',update,name='update'),
]