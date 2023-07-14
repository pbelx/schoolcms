from dataclasses import field
from pyexpat import model

from numpy import source
from rest_framework import serializers

# from . models import People
from .models import Students, SubjectTeacher, Teachers, UserRoles, PresentStudent, TimeTable, Subjects


class StudentSerial(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class TeacherSerial(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"


class PresentSerial(serializers.ModelSerializer):
    class Meta:
        model = PresentStudent
        fields = "__all__"


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = ("rname", "role", "password")


class TimeTableSerial(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = "__all__"


class SubjectSerial(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = "__all__"


class SubjectTeacherSerial(serializers.ModelSerializer):
    # Sname = serializers.CharField(source=SubjectTeacher.subjectName)

    class Meta:
        # subjectName = serializers.ReadOnlyField(source='Subjects.subjectName')
        # Sname = serializers.CharField(source=SubjectTeacher.subjectName)
        model = SubjectTeacher
        fields = ("__all__")
