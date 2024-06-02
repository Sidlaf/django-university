from collections import defaultdict

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Score, Student, Subject


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scores = Score.objects.all()
        student_scores = defaultdict(dict)
        subject_averages = defaultdict(float)
        student_averages = {}

        subjects = set()
        for score in scores:
            subject_name = score.subject.name
            subjects.add(subject_name)
            student_scores[score.student][subject_name] = score.value
            subject_averages[subject_name] += score.value

        subjects = sorted(subjects)
        for subject in subjects:
            subject_averages[subject] /= Student.objects.count()
        subject_averages = dict(subject_averages)

        student_statistics = []
        for student, scores in student_scores.items():
            student_total = 0
            for subject in subjects:
                student_total += scores.get(subject, 0)
            student_average = student_total / len(subjects)
            student_averages[student.fio] = student_average
            student_statistics.append(
                {
                    'student': student,
                    'scores': [f'{scores.get(subject, "-"):.1f}' if isinstance(scores.get(subject), (int, float)) else '-' for subject in subjects],
                    'average': f'{student_average:.1f}'
                }
            )

        best_student = max(student_averages, key=student_averages.get)
        worst_student = min(student_averages, key=student_averages.get)

        context.update(
            {
                'subjects': subjects,
                'student_statistics': student_statistics,
                'subject_averages': subject_averages,
                'best_student': best_student,
                'worst_student': worst_student,
            }
        )
        return context

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'surname', 'email']
    template_name = 'student_form.html'
    success_url = reverse_lazy('index')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'surname', 'email']
    template_name = 'student_form.html'
    success_url = reverse_lazy('index')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('index')


class SubjectCreateView(CreateView):
    model = Subject
    fields = ['name']
    template_name = 'subject_form.html'
    success_url = reverse_lazy('index')


class SubjectUpdateView(UpdateView):
    model = Subject
    fields = ['name']
    template_name = 'subject_form.html'
    success_url = reverse_lazy('index')


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subject_confirm_delete.html'
    success_url = reverse_lazy('index')


class ScoreCreateView(CreateView):
    model = Score
    fields = ['student', 'subject', 'value']
    template_name = 'score_form.html'
    success_url = reverse_lazy('index')


class ScoreUpdateView(UpdateView):
    model = Score
    fields = ['student', 'subject', 'value']
    template_name = 'score_form.html'
    success_url = reverse_lazy('index')


class ScoreDeleteView(DeleteView):
    model = Score
    template_name = 'score_confirm_delete.html'
    success_url = reverse_lazy('index')