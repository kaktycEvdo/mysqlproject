from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Person(AbstractUser):
    passport = models.CharField(primary_key=True, max_length=11, null=False, blank=False)

    email = models.CharField(max_length=50, unique=True)

    last_name = models.CharField(name="last_name", max_length=50, null=False)
    first_name = models.CharField(name="first_name", max_length=50, null=False)
    middle_name = models.CharField(name="middle_name", max_length=50)

    birth_date = models.DateField(name="birthdate", null=False, help_text="Example: 12-15-2004")
    phone_number = models.CharField(name="phonenumber", max_length=15, null=False)

    
    REQUIRED_FIELDS = [passport, email, last_name, first_name, birth_date, phone_number]

    def items(self):
        return self.__dict__


class Client(models.Model):
    client_code = models.AutoField(name="clientid", primary_key=True)

    INN = models.IntegerField(name="inn", max_length=12, null=False)
    SNILS = models.IntegerField(name="snils", max_length=11, null=False)

    person_data = models.OneToOneField("Person", on_delete=models.CASCADE, null=False, unique=True)

    
    REQUIRED_FIELDS = [INN, SNILS, person_data]

    def items(self):
        return self.__dict__

class Worker(models.Model):
    worker_code = models.AutoField(name="workerid", primary_key=True)

    specialization = models.CharField(max_length=15, null=False)
    experience = models.IntegerField(null=False)

    person_data = models.OneToOneField("Person", on_delete=models.CASCADE, null=False, unique=True)

    
    REQUIRED_FIELDS = [specialization, experience, person_data]

    def items(self):
        return self.__dict__


class Partner(models.Model):
    partner_code = models.AutoField(name="partnerid", primary_key=True)
    
    naming = models.CharField(max_length=50, null=False)
    worktime_beginning = models.TimeField(null=False)
    worktime_end = models.TimeField(null=False)
    extra_info = models.CharField(max_length=100)

    
    REQUIRED_FIELDS = [naming, worktime_beginning, worktime_end, extra_info]

    def items(self):
        return self.__dict__


class Contract(models.Model):
    contract_code = models.AutoField(name="contractid", primary_key=True)

    partners = models.ForeignKey("Partner", on_delete=models.CASCADE)
    client_code = models.OneToOneField("Client", on_delete=models.CASCADE, null=False)
    worker_code = models.OneToOneField("Worker", on_delete=models.CASCADE, null=False)
    
    service = models.CharField(max_length=50, null=False)
    date_of_upbringing = models.DateTimeField(name="dateofupbringing", null=False)


    REQUIRED_FIELDS = [partners, client_code, worker_code, service, date_of_upbringing]

    def items(self):
        return self.__dict__
