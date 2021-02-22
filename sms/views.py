from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from parsingOsonSms.parse import logining
from .models import Students, SaveMessage


def index(request):
    time = request.GET.get('time', None)
    date = request.GET.get('date', None)
    kurs = request.GET.get('kurs', None)
    group = request.GET.get('group', None)
    people = Students.objects.filter(dayOfDate=date, timeOfKurs=time, kurs=kurs, group=group)
    return render(request, "pages/students.html", {"people": people})


def listKurs(request):
    return render(request, "pages/list_kurs.html")


def sendSms(request):
    if request.is_ajax():
        if request.POST:
            pk = request.POST['pk']
            personStatus = request.POST['personStatus']
            print(pk, personStatus)
            student = Students.objects.filter(pk=pk)
            studentParentsTel = student[0].telParents
            studentname = student[0].sirname + ' ' + student[0].name + '. '
            if personStatus == 'Хаст':
                logining(studentParentsTel, studentname + 'Ба дарс хозир шуд.', params=None)
                saveMsgToServer(Students.objects.get(pk=pk), 'Ба дарс хозир шуд.')
            elif personStatus == 'Нест':
                logining(studentParentsTel, studentname + 'Ба дарс хозир НАшуд.', params=None)
                saveMsgToServer(Students.objects.get(pk=pk), 'Ба дарс хозир НАшуд.')
            else:
                logining(studentParentsTel, studentname + 'Соати дарси тамом шуд.', params=None)
                saveMsgToServer(Students.objects.get(pk=pk), 'Соати дарси тамом шуд.')
            return HttpResponse()


def saveMsgToServer(user, msg):
    msg = SaveMessage.objects.create(id_name=user, data=timezone.now(), typeOfMessage=msg)
    msg.save()