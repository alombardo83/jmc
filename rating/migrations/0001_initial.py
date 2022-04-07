# Generated by Django 3.2.12 on 2022-02-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name="nom d'utilisateur")),
                ('rating', models.PositiveSmallIntegerField()),
                ('body', models.TextField(verbose_name='avis')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='publié le')),
            ],
            options={
                'verbose_name': 'avis',
                'verbose_name_plural': 'avis',
                'ordering': ['-date'],
            },
        ),
    ]