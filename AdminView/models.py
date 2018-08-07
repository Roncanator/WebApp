from django.db import models


# Create your models here.
class LabSlot(models.Model):
    lab_time = models.TimeField('Time Chosen')
    lab_name = models.CharField(max_length=20)

    def __str__(self):
        return self.lab_name + " @ " + self.lab_time.strftime('%H:%M:%S')


class LabDemos(models.Model):
    lab = models.ForeignKey(LabSlot, on_delete=models.CASCADE)
    chosen_demos = models.CharField(max_length=200)
