from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from pollsapp.models import Question, Choice
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'pollsapp/index.html', context)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'pollsapp/detail.html', {'question' : question})

def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, "pollsapp/results.html", {"question" : question})

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExists):
        return render(request, "pollsapp/detail.html", {'question' : question,
                                                        "error_message" : "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("results", args=(question.id,)))
