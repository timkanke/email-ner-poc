from django.db import models


class Item(models.Model):
    class Status(models.IntegerChoices):
        INACTIVE = 0, "Not Started"
        ACTIVE = 1, "In Progress"
        COMPLETE = 2, "Complete"

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    pool_report = models.BooleanField(null=False)
    publish = models.BooleanField(null=False)
    off_the_record = models.BooleanField(null=False)
    review_status = models.SmallIntegerField(
        choices=Status.choices,
        blank=False,
        default="Unspecified",
        verbose_name="Editorial Review",
    )
    notes = models.TextField(max_length=1000, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
