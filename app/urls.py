from django.urls import path
from app.views import (HomePageView,AboutPageView,AppointmentListView,AppointmentDetailView,AppointmentCreateView,
                       AppointmentUpdateView, AppointmentDeleteView)

urlpatterns =[
    path('', HomePageView.as_view(), name='Home'),
    path('About/', AboutPageView.as_view(), name='About'),
    path('AppointmentList/', AppointmentListView.as_view(), name='AppointmentList'),
    path('AppointmentList/<int:pk>/',AppointmentDetailView.as_view(), name='AppointmentDetail'),
    path('AppointmentList/create', AppointmentCreateView.as_view(), name='AppointmentCreate'),
    path('AppointmentList/<int:pk>/edit',AppointmentUpdateView.as_view(), name='AppointmentUpdate'),
    path('AppointmentList/<int:pk>/delete',AppointmentDeleteView.as_view(), name='AppointmentDelete'),
]