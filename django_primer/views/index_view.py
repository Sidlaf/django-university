from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import Student, Subject, Score

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subjects = Subject.objects.all()
        students = Student.objects.all()

        student_statistics = []

        for student in students:
            scores = []
            for subject in subjects:
                score = Score.objects.filter(student=student, subject=subject).first()
                scores.append(score.value if score else '-')
            student_statistics.append({
                'student': student,
                'scores': scores
            })

        context['subjects'] = subjects
        context['student_statistics'] = student_statistics
        return context