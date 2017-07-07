from django.db import models


class CodeRun(models.Model):
    run_id = models.PositiveIntegerField()
    run_status = models.CharField(max_length=255)
    output = models.TextField()
