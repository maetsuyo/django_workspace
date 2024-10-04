from django.urls import path
from .views import FriendList, FriendDetail
from . import views
# from .views import HelloView

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('create',views.create,name='create'),
    path('edit/<int:num>',views.edit,name='edit'),
    path('delete/<int:num>',views.delete,name='delete'),
    path('list', FriendList.as_view()),
    path('detail/<int:pk>', FriendDetail.as_view()),
    path('find', views.findSql, name='find'),
    path('check', views.check, name='check'),
    path('message/', views.message, name='message'),
    path('message/<int:page>', views.message, name='message'),
    # path('<int:id>/<nickname>/', views.index, name='index'),
    # path('form', views.form, name='form'),
    # path('next', views.next, name='next'),
    # path('test', views.test, name='test'),
    # path('',HelloView.as_view(),name='index'),
]