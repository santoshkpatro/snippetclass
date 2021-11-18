from django.contrib.postgres.fields import ArrayField
from django.db import models
from . subject import Subject


class Board(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    attachments = ArrayField(models.URLField(), blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'boards'

    def __str__(self) -> str:
        return self.title
