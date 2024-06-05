from django.db import models

class Student(models.Model):
    last_name = models.CharField(max_length=200, null=False)
    first_name = models.CharField(max_length=200, null=False)
    patronymic = models.CharField(max_length=200, null=True)
    birth_date = models.DateField()
    email = models.EmailField(null=False)

    @property
    def name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}' if self.patronymic else f'{self.last_name} {self.first_name}'

    def __str__(self):
        return f'{self.fio} ({self.email})'

    def __repr__(self):
        return f'Student(last_name="{self.last_name}", first_name="{self.first_name}", patronymic="{self.patronymic}", email="{self.email}")'