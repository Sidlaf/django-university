from django.db.models import Avg, F, Value, Case, When
from django.db.models.functions import Concat
from django.views.generic import TemplateView
from ..models import Score

class ReportView(TemplateView):
    template_name = 'report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate averages for each student
        student_averages = list(
        Score.objects.annotate(
            student_name=Case(
                When(
                    student__patronymic__isnull=True,
                    then=Concat(F('student__last_name'), Value(' '), F('student__first_name'))
                    ),            
                default=Concat(F('student__last_name'), Value(' '), F('student__first_name'), Value(' '), F('student__patronymic'))
            )
        )
        .values('student_name') 
                .annotate(average_score=Avg('value'))
                .order_by('-average_score')
            )
        
        # Calculate averages for each subject
        subject_averages = list(
            Score.objects.values('subject__name')
            .annotate(average_score=Avg('value'))
            .order_by('-average_score')
        )
        
        # Safely assign best and worst student based on average score
        if student_averages:
            context['student_averages'] = student_averages
            context['best_student'] = student_averages[0]
            context['worst_student'] = student_averages[-1]
        else:
            context['student_averages'] = []
            context['best_student'] = None
            context['worst_student'] = None
            
        context['subject_averages'] = subject_averages

        return context