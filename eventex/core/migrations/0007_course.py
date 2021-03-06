# Generated by Django 3.0.3 on 2020-03-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200315_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='título')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='início')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('slots', models.IntegerField(verbose_name='vagas')),
                ('speakers', models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrantes')),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
            },
        ),
    ]
