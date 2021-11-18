from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tags'

    def __str__(self) -> str:
        return self.name
