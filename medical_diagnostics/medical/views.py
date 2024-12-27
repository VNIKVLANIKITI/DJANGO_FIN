from django.shortcuts import render
from django.http import HttpResponse
from medical.models import MedicalService, Appointment
from django.views.generic import CreateView, DeleteView, UpdateView
from medical.forms import AppointmentForm, ServiceForm
from django.urls import reverse_lazy


# Create your views here.
def check(request):
    return render(request, 'medical/base.html')


def get_services_list(request):
    services_list = MedicalService.objects.all()
    context = {
        'object_list': services_list,
        'name_list': MedicalService._meta.verbose_name_plural,
        'active_menu': 'services',
    }
    print(context)
    return render(request, 'medical/services_list_cut.html', context)

def services_list_edit(request):
    services_list = MedicalService.objects.all()
    context = {
        'object_list': services_list,
        'name_list': MedicalService._meta.verbose_name_plural,
        'active_menu': 'services',
    }
    print(context)
    return render(request, 'medical/services_list.html', context)


def get_appointments_list(request):
    appointments_list = Appointment.objects.filter(client=request.user.id)
    context = {
        'object_list': appointments_list,
        'name_list': Appointment._meta.verbose_name_plural,
        'active_menu': 'appointments',
    }
    print(context)
    return render(request, 'medical/appointments_list.html', context)


def appointments_list_edit(request):
    appointments_list = Appointment.objects.all()
    context = {
        'object_list': appointments_list,
        'name_list': Appointment._meta.verbose_name_plural,
        'active_menu': 'appointments_edit',
    }
    print(context)
    return render(request, 'medical/appointments_list_edit.html', context)


class AppointmentsCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('medical:appointments_list')

    def form_valid(self, form):
        # Устанавливаем текущего пользователя как клиента
        form.instance.client = self.request.user
        return super().form_valid(form)


class AppointmentsUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'medical/appointment_edit.html'
    success_url = reverse_lazy('medical:appointments_list')


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'medical/appointment_delete.html'
    success_url = reverse_lazy('medical:appointments_list')


class ServiceUpdateView(UpdateView):
    model = MedicalService
    form_class = ServiceForm
    template_name = 'medical/service_edit.html'
    success_url = reverse_lazy('medical:services_list')


class ServiceDeleteView(DeleteView):
    model = MedicalService
    template_name = 'medical/service_delete.html'
    success_url = reverse_lazy('medical:services_list')
