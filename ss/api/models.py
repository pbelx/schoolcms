from pyexpat import model
from re import T
from django.db import models


# Create your views here.


class Students(models.Model):

    schools = (
        ("P1", "P1"),
        ("P2", "P2"),
        ("P3", "P3"),
        ("P4", "P4"),
        ("P5", "P5"),
        ("P6", "P6"),
        ("P7", "P7"),
    )

    gender = (("B", "Boy"), ("G", "Girl"), ("N", "None"))

    firstname = models.CharField(max_length=100, default="fname")

    secondname = models.CharField(max_length=100, default="sname")
    studentbirth = models.DateField(default="1990-01-01")
    studentgender = models.CharField(max_length=1, choices=gender, default="N")
    fathersname = models.CharField(max_length=100, default="dad name")
    fathersnumber = models.IntegerField(default=200000001)
    mothersname = models.CharField(max_length=100, default="mom name")
    mothersnumber = models.IntegerField(default=10000001)
    emergencyname = models.CharField(max_length=100, default="mother mary")
    emergencyno = models.IntegerField(default=911)
    parentemail = models.CharField(max_length=100, default="test@gmail.com")
    studentclass = models.CharField(
        max_length=2, default="P1", choices=schools)
    password = models.CharField(max_length=100, default="testpass")

    def __str__(self):
        return self.firstname


class Teachers(models.Model):

    titles = (("Mr", "Mr"), ("Mrs", "Mrs"), ("Miss", "Miss"))

    maritalx = (
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorced", "Divorced"),
    )

    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    title = models.CharField(max_length=5, choices=titles)
    nin = models.CharField(max_length=100, default="0")
    dob = models.DateField
    maritals = models.CharField(max_length=50, choices=maritalx)
    address = models.CharField(max_length=100)
    contact = models.IntegerField(default=256444)
    email = models.CharField(max_length=100)
    refname = models.CharField(max_length=100)
    refcontact = models.CharField(max_length=100)

    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname


class UserRoles(models.Model):

    rolename = (
        ("teacher", "teacher"),
        ("admin", "admin"),
        ("student", "student"),
        ("support", "support"),
    )

    rname = models.CharField(max_length=100, default="")
    role = models.CharField(max_length=20, choices=rolename)
    password = models.CharField(max_length=100, default="")

    class Meta:
        ordering = ("rname",)

    def __str__(self):
        return self.rname


class PresentStudent(models.Model):

    presentchoices = (
        ("true", "true"),
        ("false", "false"),
    )
    schools = (
        ("P1", "P1"),
        ("P2", "P2"),
        ("P3", "P3"),
        ("P4", "P4"),
        ("P5", "P5"),
        ("P6", "P6"),
        ("P7", "P7"),
    )

    classdate = models.CharField(max_length=50, default=0)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    isPresent = models.CharField(
        max_length=20, choices=presentchoices, default="false")
    sid = models.CharField(
        max_length=100,
    )
    studentsubject = models.CharField(max_length=100, default="Art")
    studentclass = models.CharField(
        max_length=2, default="P1", choices=schools)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.firstname


class PresentStudent2(models.Model):

    presentchoices = (
        ("true", "true"),
        ("false", "false"),
    )
    schools = (
        ("P1", "P1"),
        ("P2", "P2"),
        ("P3", "P3"),
        ("P4", "P4"),
        ("P5", "P5"),
        ("P6", "P6"),
        ("P7", "P7"),
    )

    currentdate = models.CharField(max_length=50, default=0)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    presentstatus = models.CharField(
        max_length=20, choices=presentchoices, default="false"
    )
    sid = models.CharField(
        max_length=100,
    )
    # studentsubject = models.CharField(max_length=100, default="Art")
    studentclass = models.CharField(
        max_length=2, default="P1", choices=schools)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.firstname


class TimeTable(models.Model):

    schools = (
        ("P1", "P1"),
        ("P2", "P2"),
        ("P3", "P3"),
        ("P4", "P4"),
        ("P5", "P5"),
        ("P6", "P6"),
        ("P7", "P7"),
    )

    classdays = (
        ("monday", "monday"),
        ("tuesday", "tuesday"),
        ("wednesday", "wednesday"),
        ("thursday", "thursday"),
        ("friday", "friday"),
    )

    classTime = models.CharField(max_length=50, default=0)
    classDay = models.CharField(max_length=100, choices=classdays)
    subject = models.CharField(max_length=100)
    studentclass = models.CharField(
        max_length=20, choices=schools, default="P1")

    class Meta:
        ordering = ("classTime",)

    def __str__(self):
        return self.classDay


class Subjects(models.Model):
    subjectName = models.CharField(max_length=50, unique=True)
    subjectInfo = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.subjectName


class SubjectTeacher(models.Model):
    subjectName = models.ForeignKey(
        Subjects, on_delete=models.CASCADE, db_column="subjectName", verbose_name="subjectName")
    subjectTeacher = models.ForeignKey(
        Teachers, on_delete=models.CASCADE, db_column="firstname")

    def __str__(self):
        return self.subjectName.subjectName
