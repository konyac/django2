from django.db import models


# Create your models here.

class UserType(models.Model):
    nid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=16)

    def __str__(self):
        return "%s-%s" % (self.nid, self.caption)


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)  # email 形式只跟admin查看有关
    pwd = models.CharField(max_length=64)
    user_type = models.ForeignKey(UserType)
