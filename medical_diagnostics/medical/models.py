from django.db import models
from users.models import User


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)  # Поле с автоинкрементом
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    specialization = models.CharField(max_length=255, verbose_name='Специализация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.specialization})"


class MedicalService(models.Model):
    id = models.AutoField(primary_key=True)  # Поле с автоинкрементом
    name = models.CharField(max_length=255, verbose_name='Название услуги')
    description = models.TextField(blank=True, verbose_name='Описание услуги')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    duration = models.IntegerField(verbose_name='Продолжительность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    specialization = models.CharField(max_length=255, verbose_name='Специализация')

    class Meta:
        verbose_name = 'Медицинская услуга'
        verbose_name_plural = 'Медицинские услуги'

    def __str__(self):
        return f"{self.name} ({self.specialization})"

#  from django.contrib.auth.models import User


class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor', verbose_name='Врач')
    procedure_data = models.DateField(default='1900-01-01', verbose_name='Дата приема')
    start_time = models.TimeField(verbose_name='Время приема')
    created_at = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(MedicalService, on_delete=models.CASCADE, related_name='service', verbose_name='Процедура')

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'

    def __str__(self):
        return f"{self.client} - {self.specialist} at {self.start_time}"

'''
# Медицинские услуги:
class MedicalServices(models.Model):
    id = models.AutoField(primary_key=True)  # Поле с автоинкрементом
    # Пользователь — создатель привычки.
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Создатель')
    # Место — место, в котором необходимо выполнять привычку.    
    action_place = models.ForeignKey(place, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Место выполнения')
    # Время — время, когда необходимо выполнять привычку.
    action_time = models.TimeField(default=timezone.now, verbose_name='Время выполнения')
    # Действие — действие, которое представляет собой привычка.
    action_name = models.ForeignKey(action, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Действие')
    # Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
    is_nice = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    # Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
    habit_link = models.ForeignKey('habits.habit', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Связанная привычка')
    # Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
    periodicity_CHOICES = [
        ('every_hour', 'каждый час'),
        ('twice_day', 'дважды в день'),
        ('three_times_day', 'трижды в день'),
        ('every_day', 'каждый день'),
        ('every_two_days', 'каждые два дня'),
        ('every_three_days', 'каждые три дня'),
        ('every_five_days', 'каждые пять дней'),
        ('weekly', 'еженедельно'),
    ]
    periodicity = models.CharField(max_length=20, choices=periodicity_CHOICES, default='every_day', verbose_name='Периодичность')
    # Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
    time_long = models.IntegerField(default=0, verbose_name='Продолжительность выполнения (мин)')
    # Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
    myreward = models.ForeignKey(reward, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Вознаграждение')
    # Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.
    is_public = models.BooleanField(default=False, verbose_name='Публичная')

    def __str__(self):
        # я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
        return f" я буду {self.action_name} в {self.action_time} в {self.action_place}" 
    
    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
'''
