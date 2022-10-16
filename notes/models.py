from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    details = models.TextField(max_length=255)

