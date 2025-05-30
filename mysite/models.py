from django.db import models

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=50, blank=True)
    salary = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company' 