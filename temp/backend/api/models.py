# Create your models here.
# this defines the fields for the tables in our database
#so each model corresponds to a table

from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = 'test_database_teacher'  # Specify the custom table name

    def __str__(self):
        return self.name
