from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import Subject

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject_list.html'

class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subject_form.html'
    fields = ['name']
    success_url = reverse_lazy('subject_list')

class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'subject_form.html'
    fields = ['name']
    success_url = reverse_lazy('subject_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subject_confirm_delete.html'
    success_url = reverse_lazy('subject_list')