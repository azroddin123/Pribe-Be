# Generated by Django 4.2 on 2024-09-10 07:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='brand_logos/')),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('make', models.CharField(blank=True, max_length=128, null=True)),
                ('car_title', models.CharField(blank=True, max_length=128, null=True)),
                ('car_model', models.CharField(blank=True, max_length=128, null=True)),
                ('variant', models.CharField(blank=True, max_length=128, null=True)),
                ('vin', models.CharField(blank=True, max_length=128, null=True)),
                ('mileage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('make_year', models.PositiveIntegerField(blank=True, null=True)),
                ('body_structure_damage', models.CharField(blank=True, max_length=128, null=True)),
                ('flooded_body', models.CharField(blank=True, max_length=128, null=True)),
                ('rto_location', models.CharField(blank=True, max_length=128, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ownership', models.CharField(blank=True, max_length=128, null=True)),
                ('registration_location', models.CharField(blank=True, max_length=128, null=True)),
                ('insurance', models.CharField(blank=True, max_length=128, null=True)),
                ('insurance_validity', models.DateField(blank=True, null=True)),
                ('warranty', models.CharField(blank=True, max_length=128, null=True)),
                ('fuel_type', models.CharField(blank=True, max_length=128, null=True)),
                ('engine_capacity', models.CharField(blank=True, max_length=128, null=True)),
                ('transmission', models.CharField(blank=True, max_length=128, null=True)),
                ('condition', models.TextField(blank=True, max_length=128, null=True)),
                ('key_features', models.TextField(blank=True, max_length=128, null=True)),
                ('convenience_feature', models.TextField(blank=True, max_length=128, null=True)),
                ('km_driven', models.PositiveIntegerField(blank=True, null=True)),
                ('registry_year', models.PositiveIntegerField(blank=True, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=12, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='car_images/')),
                ('status', models.CharField(blank=True, choices=[('available', 'Available'), ('sold', 'Sold')], max_length=20, null=True)),
                ('seller_name', models.CharField(blank=True, max_length=128, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=128, null=True)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('vehicle_interest', models.CharField(blank=True, max_length=255, null=True)),
                ('inquiry_type', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.CharField(blank=True, max_length=128, null=True)),
                ('review_text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload_to')),
                ('rating', models.PositiveIntegerField(default=0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='cars.car')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('car_image', models.ImageField(upload_to='car_images')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_image', to='cars.car')),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
    ]
