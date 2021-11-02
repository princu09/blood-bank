from django.db import models

class Blood_Donor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=4)
    qty = models.CharField(max_length=4)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return f"ID : {self.id} | {self.name} : {self.blood_group}"