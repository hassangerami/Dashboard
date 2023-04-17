from django.db import models


class CreateModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class TicketModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.description[:20]}'
