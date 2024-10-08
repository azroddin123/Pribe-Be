# Generated by Django 4.2 on 2024-09-10 07:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=128, null=True)),
                ('last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.CharField(blank=True, max_length=128, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=128, null=True)),
                ('vehicle_name', models.CharField(blank=True, max_length=128, null=True)),
                ('inquiry_type', models.CharField(blank=True, max_length=128, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestDrive',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(blank=True, max_length=128, null=True)),
                ('email_address', models.CharField(blank=True, max_length=128, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=128, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=128, null=True)),
                ('car_model', models.CharField(blank=True, max_length=128, null=True)),
                ('preferred_location', models.CharField(blank=True, max_length=128, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_drive', to='cars.car')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
    ]
