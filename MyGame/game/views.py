#from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse('Hello' ,choice)
from django.template import loader
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from .models import Board


def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    return reset(request)

def reset(request):
    template = loader.get_template('game/index.html')
    b = Board.objects.all()[0]
    b.output = '#########'
    b.save()
    context = {'output' : b, 'n' : 3}
    return HttpResponse(template.render(context, request))


@csrf_exempt
def rps_post(request):
    c = {}
    c.update(csrf(request));
    data = request.POST["sel1"]
    data1 = request.POST["sel2"]
    print(data)
    print(data1)
    try:
        if data[0:-1]==data1[0:-1]:
            st = '{"data":"Both Players selected same option. It\'s a Tie","result":"tie"}'
        elif data == "rock_p1":
            if data1 == "paper_p2":
                st = '{"data":"Player 2 Wins K.O","result":"player2"}'
            else:
                st = '{"data":"Player 1 Wins K.O","result":"player1"}'
        elif data == "paper_p1":
            if data1 == "scissor_p2":
                st = '{"data":"Player 2 Wins K.O","result":"player2"}'
            else:
                st = '{"data":"Player 1 Wins K.O","result":"player1"}'
        elif data == "scissor_p1":
            if data1 == "rock_p2":
                st = '{"data":"Player 2 Wins K.O","result":"player2"}'
            else:
                st = '{"data":"Player 1 Wins K.O","result":"player1"}'
    except Exception as e:
        st = e
    return HttpResponse(st,content_type="application/type")
