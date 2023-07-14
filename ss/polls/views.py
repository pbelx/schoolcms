from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.


def hello(request):
    return HttpResponse("best at jango")


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request,):
    # context = {'qns': 'questionid'}
    return render(request, 'polls/detail.html')


def result(request, questionid):
    return HttpResponse("you are on results of question %s" % questionid)


def details(request, questionid):
    try:
        questionx = Question.objects.get(pk=questionid)
    except Question.DoesNotExist:
        return HttpResponse("Question does not exist")
    print(questionx.question)
    return render(request, 'polls/details.html', {'question': questionx})
    # return print(questionx)


def vote(request, questionid):
    return HttpResponse("you are voting on detail %s" % questionid)
