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
    username = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = "user"

    def __unicode__(self):
        return u'%s' % [self.user_id]


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        db_table = "category"

    def __unicode__(self):
        return u'%s' % [self.id]


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    boot_title = models.CharField(max_length=100)

    class Meta:
        db_table = "book"

    def __unicode__(self):
        return u'%s' % [self.id]

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)

    class Meta:
        db_table = "student"

    def __unicode__(self):
        return u'%s' % [self.id]