from django.db import models
from django.contrib.postgres.fields import ArrayField
from . assignment import Assignment
from . user import User


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    submission_text = models.TextField(blank=True, null=True)
    attachments = ArrayField(models.URLField(), blank=True, null=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        db_table = 'submissions'

    def __str__(self) -> str:
        return str(self.id)
