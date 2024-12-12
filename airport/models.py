# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employee(models.Model):
    id_employee = models.IntegerField(primary_key=True)
    full_name = models.TextField(db_column='full name')  # Field renamed to remove unsuitable characters.
    post = models.TextField()
    contact_information = models.TextField()
    id_equipage = models.ForeignKey('Equipage', models.DO_NOTHING, db_column='id_equipage')
    id_technical_staff = models.ForeignKey('TechnicalStaff', models.DO_NOTHING, db_column='id_technical_staff')

    class Meta:
        managed = False
        db_table = 'Employee'


class Equipage(models.Model):
    id_equipage = models.IntegerField(primary_key=True)
    data_formation = models.DateTimeField(blank=True, null=True)
    commander_equipage = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Equipage'


class FlightHistory(models.Model):
    id_flight_history = models.IntegerField(primary_key=True)
    id_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='id_employee')
    id_technical_staff = models.ForeignKey('TechnicalStaff', models.DO_NOTHING, db_column='id_technical_staff')
    id_shift = models.ForeignKey('Shift', models.DO_NOTHING, db_column='id_shift')
    id_race = models.ForeignKey('Race', models.DO_NOTHING, db_column='id_race')

    class Meta:
        managed = False
        db_table = 'Flight_history'


class Plane(models.Model):
    id_plane = models.IntegerField(primary_key=True)
    number_registration = models.TextField()
    type_plane = models.TextField()
    year_production = models.TextField()

    class Meta:
        managed = False
        db_table = 'Plane'


class Race(models.Model):
    id_race = models.IntegerField(primary_key=True)
    number_race = models.TextField()
    date_and_time_of_departure = models.DateTimeField()
    direction = models.TextField()
    id_plane = models.ForeignKey(Plane, models.DO_NOTHING, db_column='id_plane')
    id_equipage = models.ForeignKey(Equipage, models.DO_NOTHING, db_column='id_equipage')
    id_takeoff_lane = models.ForeignKey('TakeoffLane', models.DO_NOTHING, db_column='id_takeoff_lane')

    class Meta:
        managed = False
        db_table = 'Race'


class Shift(models.Model):
    id_shift = models.IntegerField(primary_key=True)
    time_start = models.TimeField()
    time_end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'Shift'


class TakeoffLane(models.Model):
    id_takeoff_lane = models.IntegerField(primary_key=True)
    category_strips = models.TextField()
    length = models.IntegerField()
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'Takeoff_lane'


class TechnicalStaff(models.Model):
    id_technical_staff = models.IntegerField(primary_key=True)
    education = models.TextField()
    experience = models.IntegerField()
    id_shift = models.ForeignKey(Shift, models.DO_NOTHING, db_column='id_shift')
    id_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='id_employee', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Technical_staff'
