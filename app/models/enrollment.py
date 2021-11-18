from django.db import models
from . subject import Subject
from . user import User


class Enrollment(models.Model):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('instructor', 'instructor')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default='student', choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'enrollments'

    def __str__(self) -> str:
        return str(self.id)
