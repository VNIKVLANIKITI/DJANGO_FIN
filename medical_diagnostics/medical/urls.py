from django.urls import path
from medical.apps import MedicalConfig
from medical.views import check, get_services_list, get_appointments_list, AppointmentsCreateView, AppointmentsUpdateView, AppointmentDeleteView, services_list_edit, appointments_list_edit, ServiceUpdateView, ServiceDeleteView

app_name = MedicalConfig.name

urlpatterns = [
    path('', check),
    path("services/", get_services_list, name='services_list'),
    path("appointments/", get_appointments_list, name='appointments_list'),
    path("appointments_edit/", appointments_list_edit, name='appointments_list_edit'),    
    path("appointments/create", AppointmentsCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>', AppointmentsUpdateView.as_view(),name='appointment_update'),
    path('appointments/delete/<int:pk>', AppointmentDeleteView.as_view(), name='appointment_delete'),
    path("services_edit/", services_list_edit, name='services_list_edit'),
    path('service/<int:pk>', ServiceUpdateView.as_view(),name='service_update'),
    path('service/delete/<int:pk>', ServiceDeleteView.as_view(), name='service_delete'),
]
