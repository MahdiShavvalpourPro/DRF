from importlib.metadata import requires

from django.db import models


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=350, null=True, blank=True)
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title} / Is Done : {self.is_done}'

    class Meta:
        db_table = 'todos'




