# Generated by Django 2.2.2 on 2019-07-18 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsamuems', '0002_auto_20190716_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creadoEn', models.DateTimeField(auto_now_add=True)),
                ('nombreArchivo', models.CharField(max_length=100)),
                ('cedulaPaciente', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
    ]
