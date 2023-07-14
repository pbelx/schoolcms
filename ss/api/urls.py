from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all", views.allpeople, name="all"),
    path("all/<pk>", views.Allgirls, name="boy girl"),
    path("class/<pk>", views.StudentClass, name="student class"),
    path("nall", views.numberpeople, name="numberp"),
    path("pinfo/<pk>", views.person_details, name="pdetails"),
    path("create", views.create, name="create"),
    path("update/<pk>", views.update, name="update"),
    path("delete/<pk>", views.delete, name="delete"),
    path("t", views.allteachers, name="teachers"),
    path("t/nall", views.numberteachers, name="numberteachers"),
    path("t/create", views.tcreate, name="teacher create"),
    path("t/<pk>", views.teacher_details, name="teacher details"),
    path("t/update/<pk>", views.tupdate, name="teacher update"),
    path("t/delete/<pk>", views.tdelete, name="teacher delete"),
    # user new
    path("roles/new/", views.NewUser.as_view()),  # create new user
    path("roles/n/", views.NUser.as_view()),  # create new user
    path("roles/", views.NUser.as_view()),  # create new user
    path("roles/<pk>", views.GetUser),  # create new user
    # attendance
    path("attend/all", views.PresentStatus.as_view()),
    path("attend/new", views.PresentStatus.as_view()),
    path("attend/a", views.GetPresentStatus),
    path("attend/n", views.CreatePresentStatus),
    path("attend/class/<pk>", views.PresentClass),  # filter class
    path("attend/date/<pk>", views.PresentDate),  # filter date
    path("attend/subject/<pk>", views.PresentSubject),  # filter subject
    path("attend/status/<pk>", views.PresentStatusClass),  # filter status
    path("attend/id/<pk>", views.PresentId),  # filter status
    # timetable
    path("timetable/", views.TimeTableStatus.as_view()),  # create new user
    path("timetable/class/<pk>", views.TimeTableClass),  # filter subject
    path("timetable/del/<pk>", views.TimeTableDelete),  # filter subject

    # subjects area
    path("subjects/", views.SubjectView.as_view()),  # view subjects
    path("subjects/delete/<pk>", views.subjectdelete),  # delete subjects
    path("subjects/detail/<pk>", views.subjectdetails),  # delete subjects
    # teacher sub assign view
    path("subjects/teacher", views.SubjectTeacherView.as_view())

]
