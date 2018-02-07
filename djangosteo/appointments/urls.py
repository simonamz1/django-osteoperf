from django.urls import path

from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.AppointmentListView.as_view(), name='list'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='detail'),
    path('create/', views.AppointmentCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.AppointmentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AppointmentDeleteView.as_view(), name='delete'),
]
