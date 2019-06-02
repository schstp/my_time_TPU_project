# Generated by Django 2.2 on 2019-06-02 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='timestemp',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='content',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='author',
            new_name='user',
        ),
        migrations.AddField(
            model_name='task',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='task',
            name='lists',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.List'),
        ),
    ]
