from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import Score, Student, Subject

class ScoreListView(ListView):
    model = Score
    template_name = 'score_list.html'

class ScoreCreateView(CreateView):
    model = Score
    template_name = 'score_form.html'
    fields = ['student', 'subject', 'value']
    success_url = reverse_lazy('score_list')

class ScoreUpdateView(UpdateView):
    model = Score
    template_name = 'score_form.html'
    fields = ['student', 'subject', 'value']
    success_url = reverse_lazy('score_list')

class ScoreDeleteView(DeleteView):
    model = Score
    template_name = 'score_confirm_delete.html'
    success_url = reverse_lazy('score_list')