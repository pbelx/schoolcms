from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from .serial import StudentSerial, SubjectSerial, SubjectTeacherSerial
from .serial import TeacherSerial, UserSerial, PresentSerial, TimeTableSerial
from .models import Students, SubjectTeacher, Subjects
from .models import Teachers, UserRoles, PresentStudent, TimeTable

# api stuff route


@api_view(["GET"])
def index(request):
    return Response(
        """[{'get':'all'},
        {'get':'pinfo/pk'},
        {'create':''},
        {'update':'update/pk'},
        {'delete':'delete/pk'},
        ]"""
    )


# all people
@api_view(["GET"])
def allpeople(request):
    people = Students.objects.all()
    serial = StudentSerial(people, many=True)
    # print(len(serial.data))
    return Response(serial.data)


# all people
@api_view(["GET"])
def numberpeople(request):
    people = Students.objects.all()
    serial = StudentSerial(people, many=True)
    # print(len(serial.data))
    return Response(len(serial.data))


# single person
@api_view(["GET"])
def person_details(request, pk):
    try:
        people = Students.objects.get(id=pk)
        serial = StudentSerial(people, many=False)
        return Response(serial.data)

    except:
        return Response("no data")


# create person
@api_view(["POST"])
def create(request):
    people = request.data
    serial = StudentSerial(data=people)
    if serial.is_valid():
        serial.save()
        return Response(serial.data)


# update person
@api_view(["POST"])
def update(request, pk):
    pid = Students.objects.get(id=pk)
    people = request.data
    serial = StudentSerial(instance=pid, data=people)
    if serial.is_valid():
        serial.save()
        return Response("data saved")


# delete person
@api_view(["DELETE"])
def delete(request, pk):
    try:
        person = Students.objects.get(id=pk)
        person.delete()
        return Response("user deleted")
    except:
        return Response("no data to delete")


# teachers section


# get all
@api_view(["GET"])
def allteachers(request):
    people = Teachers.objects.all()
    serial = TeacherSerial(people, many=True)
    return Response(serial.data)


# number teachers all
@api_view(["GET"])
def numberteachers(request):
    people = Teachers.objects.all()
    serial = TeacherSerial(people, many=True)
    return Response(len(serial.data))


# create user
@api_view(["POST"])
def tcreate(request):
    people = request.data
    serial = TeacherSerial(data=people)
    if serial.is_valid():
        serial.save()
        return Response(serial.data)


# get teacher details
@api_view(["GET"])
def teacher_details(request, pk):
    try:
        people = Teachers.objects.get(id=pk)
        serial = TeacherSerial(people, many=False)
        return Response(serial.data)

    except:
        return Response("no data")


# girls only
@api_view(["GET"])
def allgirls(request, pk):
    try:
        people = Students.objects.all(gender=pk)
        serial = StudentSerial(people, many=True)
        return Response(serial.data)

    except:
        return Response("no data")


# update teacher
@api_view(["POST"])
def tupdate(request, pk):
    pid = Teachers.objects.get(id=pk)
    people = request.data
    serial = TeacherSerial(instance=pid, data=people)
    if serial.is_valid():
        serial.save()
        return Response("data saved")


# delete teacher
@api_view(["POST"])
def tdelete(request, pk):
    try:
        person = Teachers.objects.get(id=pk)
        person.delete()
        return Response("user deleted")
    except:
        return Response("no data to delete")


# user roles get user
@api_view(["GET"])
def GetUser(request, pk):
    products = UserRoles.objects.filter(rname=pk)
    serialkiller = UserSerial(products, many=True)
    return Response(serialkiller.data)


# filter girls n boys
@api_view(["GET"])
def Allgirls(request, pk):

    people = Students.objects.filter(studentgender=pk)
    serial = StudentSerial(people, many=True)
    return Response(serial.data)


# filter class
@api_view(["GET"])
def StudentClass(request, pk):

    people = Students.objects.filter(studentclass=pk)
    serial = StudentSerial(people, many=True)
    return Response(serial.data)


# create user using generics
class NewUser(generics.ListCreateAPIView):
    queryset = UserRoles.objects.all()
    serializer_class = UserSerial


class NUser(generics.ListCreateAPIView):
    queryset = UserRoles.objects.all()
    serializer_class = UserSerial


# present status
class PresentStatus(generics.ListCreateAPIView):
    queryset = PresentStudent.objects.all
    serializer_class = PresentSerial


# timetable status
class TimeTableStatus(generics.ListCreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerial


# create present using decorators


@api_view(["POST"])
def CreatePresentStatus(request):
    # pstatus = PresentStudent.objects.all()
    serializer = PresentSerial(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response("Data was saved")
    else:
        return Response("not saved")


@api_view(["GET"])
def GetPresentStatus(request):
    pstatus = PresentStudent.objects.all()
    serializer = PresentSerial(pstatus, many=True)
    return Response(serializer.data)


# filter class present
@api_view(["GET"])
def PresentClass(request, pk):

    people = PresentStudent.objects.filter(studentclass=pk)
    serial = PresentSerial(people, many=True)
    return Response(serial.data)


# filter class present date
@api_view(["GET"])
def PresentDate(request, pk):

    people = PresentStudent.objects.filter(classdate=pk)
    serial = PresentSerial(people, many=True)
    return Response(serial.data)


# filter class present or not
@api_view(["GET"])
def PresentStatusClass(request, pk):

    people = PresentStudent.objects.filter(isPresent=pk)
    serial = PresentSerial(people, many=True)
    return Response(serial.data)


# filter subject
@api_view(["GET"])
def PresentSubject(request, pk):

    subject = PresentStudent.objects.filter(studentsubject=pk)
    serial = PresentSerial(subject, many=True)
    return Response(serial.data)


# filter student id
@api_view(["GET"])
def PresentId(request, pk):

    subject = PresentStudent.objects.filter(sid=pk)
    serial = PresentSerial(subject, many=True)
    return Response(serial.data)


# filter timetable by class P2 etc
@api_view(["GET"])
def TimeTableClass(request, pk):

    subject = TimeTable.objects.filter(studentclass=pk)
    serial = TimeTableSerial(subject, many=True)
    return Response(serial.data)


# filter timetable by class P2 etc
@api_view(["POST"])
def TimeTableDelete(request, pk):

    try:
        person = TimeTable.objects.get(id=pk)
        person.delete()
        return Response("user deleted")
    except:
        return Response("no data to delete")

# subjects area


class SubjectView(generics.ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerial


class SubjectDetail(generics.RetrieveDestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerial

    def get_queryset(self):
        # Assuming your `Video` model has a many-to-one relation to `Collection`
        return self.queryset.filter(
            collection__pk=self.kwargs['pk']
        )

# delete subject


class SubjectTeacherView(generics.ListCreateAPIView):
    queryset = SubjectTeacher.objects.all()
    serializer_class = SubjectTeacherSerial


@api_view(["POST"])
def subjectdelete(request, pk):
    try:
        subject = Subjects.objects.get(id=pk)
        subject.delete()
        return Response("subject deleted")
    except:
        return Response("no data to delete")


@api_view(["GET"])
def subjectdetails(request, pk):
    subject = Subjects.objects.get(id=pk)
    serial = SubjectSerial(subject)
    return Response(serial.data)

# teacher subject assign
