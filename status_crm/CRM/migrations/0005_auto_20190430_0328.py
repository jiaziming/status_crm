# Generated by Django 2.2 on 2019-04-30 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0004_auto_20190430_0323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('view_customer_list', '查看用户信息列表'), ('view_customer_info', '查看用户详情'), ('edit_own_customers_info', '修改客户信息'))},
        ),
    ]