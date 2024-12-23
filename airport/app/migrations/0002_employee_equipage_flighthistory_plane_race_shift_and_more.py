# Generated by Django 4.0.10 on 2024-12-12 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id_employee', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.TextField(db_column='full name')),
                ('post', models.TextField()),
                ('contact_information', models.TextField()),
            ],
            options={
                'db_table': 'Employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipage',
            fields=[
                ('id_equipage', models.IntegerField(primary_key=True, serialize=False)),
                ('data_formation', models.DateTimeField(blank=True, null=True)),
                ('commander_equipage', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Equipage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FlightHistory',
            fields=[
                ('id_flight_history', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Flight_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id_plane', models.IntegerField(primary_key=True, serialize=False)),
                ('number_registration', models.TextField()),
                ('type_plane', models.TextField()),
                ('year_production', models.TextField()),
            ],
            options={
                'db_table': 'Plane',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id_race', models.IntegerField(primary_key=True, serialize=False)),
                ('number_race', models.TextField()),
                ('date_and_time_of_departure', models.DateTimeField()),
                ('direction', models.TextField()),
            ],
            options={
                'db_table': 'Race',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id_shift', models.IntegerField(primary_key=True, serialize=False)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
            ],
            options={
                'db_table': 'Shift',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TakeoffLane',
            fields=[
                ('id_takeoff_lane', models.IntegerField(primary_key=True, serialize=False)),
                ('category_strips', models.TextField()),
                ('length', models.IntegerField()),
                ('status', models.TextField()),
            ],
            options={
                'db_table': 'Takeoff_lane',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TechnicalStaff',
            fields=[
                ('id_technical_staff', models.IntegerField(primary_key=True, serialize=False)),
                ('education', models.TextField()),
                ('experience', models.IntegerField()),
            ],
            options={
                'db_table': 'Technical_staff',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
    ]
