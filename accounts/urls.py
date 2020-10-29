from django.urls import path, include

from accounts import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('request_list/',views.TraineRequestListView.as_view(),name='request_list'),
    path('submit_request/',views.SubmitRequestView.as_view(),name='submit_request')
]
