# Generated by Django 3.2.8 on 2022-03-23 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20220323_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='app.user'),
        ),
    ]
