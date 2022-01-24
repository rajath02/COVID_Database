from django.db import models

# Create your models here.

class newcases(models.Model):
    name = models.CharField(max_length=50, default="")
    patient_id = models.CharField(max_length=5, primary_key=True)
    age = models.CharField(max_length=3, default="")
    gender = models.CharField(max_length=6, default="")
    address = models.CharField(max_length=50, default="")
    phone_no = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.patient_id

class recovery(models.Model):
    name = models.CharField(max_length=50, default="")
    patient_id = models.ForeignKey(newcases, on_delete=models.CASCADE)
    age = models.CharField(max_length=3, default="")
    gender = models.CharField(max_length=6, default="")
    address = models.CharField(max_length=50, default="")
    phone_no = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.patient_id)

class deaths(models.Model):
    name = models.CharField(max_length=50, default="")
    patient_id = models.ForeignKey(newcases, on_delete=models.CASCADE)
    age = models.CharField(max_length=3, default="")
    gender = models.CharField(max_length=6, default="")
    address = models.CharField(max_length=50, default="")
    phone_no = models.CharField(max_length=10, default="")
    date = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.patient_id)

class vaccine(models.Model):
    patient_id = models.ForeignKey(newcases, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=20, default="")
    dose = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.patient_id)
