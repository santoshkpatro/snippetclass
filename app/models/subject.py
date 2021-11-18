from django.db import models


class Subject(models.Model):
    subject_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    profile = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subjects'

    def __str__(self) -> str:
        return self.name
