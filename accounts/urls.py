from django.urls import path, include

from accounts import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('request_list/',views.TraineRequestListView.as_view(),name='request_list'),
    path('submit_request/',views.SubmitRequestView.as_view(),name='submit_request'),
    path('submit_request/update/<pk>',views.SubmitRequestUpdateView.as_view(),name='request_update'),
    path('submit_request/delete/<pk>',views.SubmitRequestDeleteView.as_view(),name='request_delete'),
    path('user-info/<pk>/<username>/',views.UserInfo.as_view(),name='profile'),
    path('user-info/edit/<pk>/<username>/',views.profile_edit,name='profile-edit'),
]
