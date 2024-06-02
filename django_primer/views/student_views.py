from django.urls import reverse_lazy
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
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')


class StudentPerformanceSummaryView(TemplateView):
    template_name = 'student_performance_summary.html'

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