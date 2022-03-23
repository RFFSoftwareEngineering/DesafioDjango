# Generated by Django 3.2.8 on 2022-03-23 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_megaprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('MsgBody', models.TextField(max_length=550, verbose_name='Msg')),
                ('Likes', models.ManyToManyField(blank=True, default=None, related_name='FeedPost', to='app.User')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('Msg', models.CharField(max_length=120, verbose_name='comment')),
                ('LikesComm', models.ManyToManyField(blank=True, default=None, related_name='Comments', to='app.User')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
