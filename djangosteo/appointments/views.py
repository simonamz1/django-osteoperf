from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
    )


from . import models

def appointment_list(request):
    appointments = models.Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})


def appointment_detail(request, pk):
    appointment = get_object_or_404(models.Appointment, pk=pk)
    return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})

class AppointmentListView(ListView):
    context_object_name = "appointments"
    model = models.Appointment


class AppointmentDetailView(DetailView):
    pk_url_kwarg = 'pk'
    model = models.Appointment


class AppointmentCreateView(CreateView):
    fields = ('slot', 'practitioner', 'practice_location')
    model = models.Appointment


class AppointmentUpdateView(UpdateView):
    fields = ('slot', 'practitioner', 'practice_location')
    model = models.Appointment


class AppointmentDeleteView(DeleteView):
    model = models.Appointment
    success_url = reverse_lazy("appointments:list")
