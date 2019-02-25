from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from .models import Question, Choice

# Create your views here.

def index(request):
    latastQuestionList = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latastQuestionList': latastQuestionList
    })
    return HttpResponse(template.render(context))
    # output = ','.join([p.question_text for p in latastQuestionList])
    # return HttpResponse(output)

def indexRender(request):
    latastQuestionList = Question.objects.order_by('-pub_date')[:5]
    context = {"latastQuestionList": latastQuestionList}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You`re looking at qustion %s." % question_id)

def detail404(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {"question": question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)

    try:
        selectChoice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message':"You did`t select a choice."
        })
    else:
        selectChoice.votes += 1
        selectChoice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
