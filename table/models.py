from django.db import models
from django.contrib.auth.models import AbstractUser


class Table(models.Model):
    tab_name = models.CharField(max_length=64, primary_key=True)  # '表名'
    tab_comment = models.CharField(max_length=1024)  # '表说明'
    tab_ver = models.IntegerField()  # '版本号，系统自动记录'
    tab_buzz = models.SmallIntegerField()  # '业务类型， 0 字典类，1 居民健康档案 2慢病  3 老年人 4 妇幼、儿童 5 家庭医生签约 9 其他'
    tab_type = models.SmallIntegerField(default=1)  # '类型， 1表 TABLE， 2 视图 VIEW'
    tab_status = models.SmallIntegerField(default=1)  # '表状态， 默认为1 启用， 0为不使用'
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.tab_name

    class Meta:
        ordering = ['tab_name']
        db_table = 'ehr_tables'


class Column(models.Model):
    auto_id = models.IntegerField(primary_key=True)  # 主键
    tab_name = models.CharField(max_length=64)  # '表名'
    col_name = models.CharField(max_length=64)  # '字段名'
    col_comment = models.CharField(max_length=1024)  # '字段说明'
    col_ver = models.IntegerField()  # '版本号，系统自动记录'
    data_type = models.CharField(max_length=64)  # '数据类型, 借用类型'
    is_nullable = models.SmallIntegerField(default=1)  # '是否可以为空, 默认可以为空',
    col_status = models.SmallIntegerField(default=1)  # '字段状态， 默认为1 启用， 0为不使用'
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.col_name

    class Meta:
        ordering = ['auto_id']
        db_table = 'ehr_columns'


# Custom user model
class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass
