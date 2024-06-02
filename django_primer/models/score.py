from django.db import models
from .student import Student
from .subject import Subject

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.value}"