from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.core.validators import RegexValidator

from django.db import models

SPECIALIZATION_CHOICES = (
    ('BA', 'Backache'),
    ('CR', 'Cranial Osteopathy'),
    ('PE', 'Pediatrics Osteopathy'),
    ('PR', 'Pregnancy Osteopathy'),
    ('SP', 'Sport Osteopathy'),
    ('ST', 'Structural Osteopathy'),
    ('TO', 'Torticollis'),
    ('VI', 'Visceral Osteopathy'),
)



class Specialization(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title',]


class Appointment(models.Model):
    slot = models.DateTimeField()
    practitioner = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    practice_location = models.CharField(max_length=255)
    specialization = models.ForeignKey(Specialization, verbose_name="Specialization", on_delete=models.CASCADE)

    def __int__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("appointments:list")


class Practitioner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(verbose_name='Phone Number', validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    birth_date = models.DateField(verbose_name='Date of Birth', auto_now=False)
    address = models.CharField(verbose_name='Postal Address', max_length=255)
    skills = models.ManyToManyField(Specialization, verbose_name='Medical Specializations')
    diploma = models.CharField(verbose_name='Diploma', max_length=255)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(verbose_name='Phone Number', validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    birth_date = models.DateField(verbose_name='Date of Birth', auto_now=False)
    address = models.CharField(verbose_name='Postal Address', max_length=255)

    def __str__(self):
        return self.user.username
