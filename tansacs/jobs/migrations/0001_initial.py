# Generated by Django 4.2.7 on 2023-11-29 19:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jobs.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='Experience/')),
            ],
        ),
        migrations.CreateModel(
            name='HSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
                ('register_number', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField(validators=[jobs.validators.validate_year])),
                ('percentage', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('board', models.CharField(choices=[('State Board', 'State'), ('CBSE', 'Cbse'), ('ICSE', 'Icse'), ('Matric', 'Matric')])),
                ('marksheet', models.ImageField(blank=True, null=True, upload_to='HSC/')),
            ],
        ),
        migrations.CreateModel(
            name='PG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
                ('register_number', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField(validators=[jobs.validators.validate_year])),
                ('percentage', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('marksheet', models.ImageField(blank=True, null=True, upload_to='PG/')),
            ],
        ),
        migrations.CreateModel(
            name='PreferedExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(choices=[('NACO', 'Naco'), ('TANSACS', 'Tansacs'), ('TSU', 'Tsu')], max_length=100)),
                ('year', models.IntegerField()),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='PreferedExperience/')),
                ('NOC', models.ImageField(blank=True, null=True, upload_to='NOC/')),
            ],
        ),
        migrations.CreateModel(
            name='SSLC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
                ('register_number', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField(validators=[jobs.validators.validate_year])),
                ('percentage', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('board', models.CharField(choices=[('State Board', 'State'), ('CBSE', 'Cbse'), ('ICSE', 'Icse'), ('Matric', 'Matric')])),
                ('marksheet', models.ImageField(blank=True, null=True, upload_to='SSLC/')),
            ],
        ),
        migrations.CreateModel(
            name='UG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
                ('register_number', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField(validators=[jobs.validators.validate_year])),
                ('percentage', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('marksheet', models.ImageField(blank=True, null=True, upload_to='UG/')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.CharField(default='TAN00000', max_length=50)),
                ('mark', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)])),
                ('position', models.CharField(choices=[('Cluster Program Manager', 'Cluster Manager'), ('Clinical Service Officer', 'Clinical Officer'), ('Data Monitoring Documentation Officer', 'Data Monitoring Officer'), ('Deputy Director (LS)', 'Deputy Ls Director'), ('Deputy Director (SI)', 'Deputy Si Director'), ('Assistent Director (ICTC)', 'Assistant Ictc Director'), ('Assistent Director (TI)', 'Assistant Ti Director'), ('Assistent Director (IEC)', 'Assistant Iec Director')], max_length=100)),
                ('experience', models.ManyToManyField(related_name='detailOfJob_experience', to='jobs.experience')),
                ('hsc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detailOfJob_hsc', to='jobs.hsc')),
                ('pg', models.ManyToManyField(related_name='detailOfJob_pg', to='jobs.pg')),
                ('prefered_experience', models.ManyToManyField(related_name='detailOfJob_prefered_experience', to='jobs.preferedexperience')),
                ('sslc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detailOfJob_sslc', to='jobs.sslc')),
                ('ug', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detailOfJob_ug', to='jobs.ug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
