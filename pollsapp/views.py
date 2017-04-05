from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from pollsapp.models import Question, Choice
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = "pollsapp/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "pollsapp/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "pollsapp/results.html"

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "pollsapp/detail.html", {'question': question,
                                                        'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("results", args=(question.id,)))
