# Generated by Django 3.1.2 on 2020-11-01 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201031_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': '   Branches'},
        ),
        migrations.AlterModelOptions(
            name='designation',
            options={'verbose_name_plural': '     Designations'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': ' Profiles'},
        ),
        migrations.AlterModelOptions(
            name='training_title',
            options={'verbose_name_plural': '  Training Titles'},
        ),
        migrations.AlterModelOptions(
            name='zone',
            options={'verbose_name_plural': '    Zones'},
        ),
        migrations.AddField(
            model_name='trainerequest',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]