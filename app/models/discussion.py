from django.db import models
from . subject import Subject
from . user import User


class Discussion(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_valid = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'discussions'

    def __str__(self) -> str:
        return str(self.id)
