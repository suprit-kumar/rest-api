from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=True, default="")
    city = models.CharField(max_length=1000, null=True, default="")
    state = models.CharField(max_length=1000, null=True, default="")
    about = models.CharField(max_length=1000, null=True, default="")
    status = models.CharField(max_length=50, null=True, default="")
    user_created_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "user"

    def __unicode__(self):
        return u'%s' % [self.user_id]