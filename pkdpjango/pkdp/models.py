from django.db import models

# Create your models here.
class Member(models.Model):
        mem_name = models.CharField(max_length = 20)
        mem_age = models.IntegerField()
        mem_email = models.CharField(max_length = 20)

        def __str__(self):
            return self.mem_name
