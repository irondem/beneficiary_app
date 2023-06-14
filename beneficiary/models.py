from django.db import models

class Household(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    is_recipient = models.BooleanField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AssistanceProject(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    assistance_project = models.ForeignKey(AssistanceProject, on_delete=models.CASCADE)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    cash_offer = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Enrollment {self.id}"
