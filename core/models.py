from __future__ import unicode_literals

import uuid

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


class BaseModel(models.Model):
    """ abstract class defining common fields """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, default=timezone.now)
    last_modified_on = models.DateTimeField(auto_now=True, default=timezone.now)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class School(BaseModel):
    """ school """
    name = models.CharField(max_length=150)

    def __str__(self):
        """ object representation """
        return "<School: {}>".format(self.name)


@python_2_unicode_compatible
class Standard(BaseModel):
    """ standard """
    school = models.ForeignKey(School)
    name = models.CharField(max_length=20)

    def __str__(self):
        """ object representation """
        return "<Standard: {}>".format(self.name)


@python_2_unicode_compatible
class Division(BaseModel):
    """ division """
    standard = models.ForeignKey(Standard)
    name = models.CharField(max_length=20)
    staff_in_charge = models.ForeignKey(Staff)

    def __str__(self):
        """ object representation """
        return "<Division: {}>".format(self.name)


@python_2_unicode_compatible
class Student(BaseModel):
    """ student """
    division = models.ForeignKey(Division)
    name = models.CharField(max_length=80)

    def __str__(self):
        """ object representation """
        return "<Student: {}>".format(self.name)


@python_2_unicode_compatible
class Parent(BaseModel):
    """ parent """
    child = models.ForeignKey(Student)
    name = models.CharField(max_length=80)
    occupation = models.CharField(max_length=80)
    contact_number = models.CharField(max_length=15)
    email_id = models.EmailField()

    def __str__(self):
        """ object representation """
        return "<Parent: {}>".format(self.name)


@python_2_unicode_compatible
class Staff(BaseModel):
    """ staff """
    type = models.CharField(max_length=80, choices=(('Teaching', 'TEACHING'), ('Non Teaching', 'NON_TEACHING')))
    name = models.CharField(max_length=80)
    contact_number = models.CharField(max_length=15)
    email_id = models.EmailField()

    def __str__(self):
        """ object representation """
        return "<Staff: {}>".format(self.name)
