from django.db import models


class User(models.Model):
    user_id = models.IntegerField(default=0)
    stream_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user_id)


class Stream(models.Model):
    stream_id = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    stream_duration = models.IntegerField(default=0)
    user_count = models.IntegerField(default=0)
    sales_count = models.IntegerField(default=0)

    conversion = models.FloatField(default=0)

    def __str__(self):
        return str(self.stream_id)
