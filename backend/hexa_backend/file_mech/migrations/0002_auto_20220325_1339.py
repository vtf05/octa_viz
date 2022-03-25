# Generated by Django 3.2.7 on 2022-03-25 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_mech', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createfile',
            name='relevant',
        ),
        migrations.CreateModel(
            name='related_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_mech.createfile')),
            ],
        ),
    ]
