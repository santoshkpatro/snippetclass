from django.db import models
from . subject import Subject
from . tag import Tag


class Assignment(models.Model):
    subject = models.ForeignKey(Subject)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    attachment = models.URLField(blank=True, null=True)
    submission_due = models.DateTimeField(blank=True, null=True)
    allow_submission_after_due = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    tags = models.ManyToManyField(Tag, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'assignments'

    def __str__(self) -> str:
        return self.title
