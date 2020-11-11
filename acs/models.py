from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=70)
  date_of_birth = models.DateField()
  matric_no = models.CharField(max_length=16)
  fingerprint = models.ImageField(upload_to='finger-print')

  fprint_base64 = models.TextField()
  profile_pic = models.ImageField(upload_to='profile-pic')


  def __str__(self):
    return self.name


class Tracker(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  time_in = models.DateTimeField(blank=True, null=True)
  time_out = models.DateTimeField(blank=True, null=True)
  where = models.CharField(default="FSSE", max_length=4)

  def __str__(self):
    return f"{self.student.name} {self.pk}"