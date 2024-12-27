from django import forms
from medical.models import Appointment, Doctor, MedicalService


# class MailingForm(forms.ModelForm):
#     class Meta:
#         model = Mailing
#         fields = '__all__'
#         exclude = ['creator', 'attemtps']  # Исключаем поле creator из формы


# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'specialist', 'procedure_data', 'start_time']
        widgets = {
            'procedure_data': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = MedicalService
        fields = '__all__'
        # widgets = {
        #     'procedure_data': forms.DateInput(attrs={'type': 'date'}),
        #     'start_time': forms.TimeInput(attrs={'type': 'time'}),
        # }
