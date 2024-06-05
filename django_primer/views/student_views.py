from django.urls import reverse_lazy
from django import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView
from ..models import Student, Subject, Score

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['name', 'birth_date']
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['name', 'birth_date']
    widgets = {
    'birth_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
}
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

