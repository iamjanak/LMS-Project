from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Quiz, Question

@login_required
def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})

@login_required
def student_portal(request):
    courses = Course.objects.all()
    return render(request, 'courses/student_portal.html', {'courses': courses})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'courses/register.html', {'form': form})

@login_required
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        total = questions.count()
        for question in questions:
            selected_choice_id = request.POST.get(str(question.id))
            if selected_choice_id:
                choice = question.choices.get(id=selected_choice_id)
                if choice.is_correct:
                    score += 1
        return render(request, 'courses/quiz_result.html', {
            'quiz': quiz,
            'score': score,
            'total': total,
        })

    return render(request, 'courses/quiz_detail.html', {
        'quiz': quiz,
        'questions': questions,
    })