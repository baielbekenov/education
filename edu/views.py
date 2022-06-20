from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from edu.forms import RazdelForm, UserRegisterForm, TaskCreateForm, HomeworkSendForm
from edu.models import Task, Razdel, User, Homework, Teacher
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    razdel = Razdel.objects.all()
    context = {'razdel': razdel}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def homework(request, pk):
    homework = Homework.objects.all()
    context = {'homework': homework}
    return render(request, 'homework.html', context)


@login_required(login_url='login')
def create(request):
    if request.user.is_teacher:
        form = RazdelForm()
        if request.method == 'POST':
            print(request.POST)
            form = RazdelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

        context = {'form': form}

        return render(request, 'create.html', context)
    return HttpResponse('impossible to create!')

@login_required(login_url='login')
def createtask(request):
    if request.user.is_teacher:
        form = TaskCreateForm()
        if request.method == 'POST':
            print(request.POST)
            form = TaskCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse('Успешно добавлено')
        context = {'form': form}

        return render(request, 'createtask.html', context)
    return HttpResponse('impossible to create!')


@login_required(login_url='login')
def detail(request, pk):
    tasks = Task.objects.filter(razdel_id=pk).order_by('-id')
    context = {'tasks': tasks}
    return render(request, 'Detail.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':  # Проверка запроса на пост
            form = UserRegisterForm(request.POST)  # присваиваем форму для данных
            print('POST')
            if form.is_valid():  # Проверка на валидность
                form.save()  # Сохранение в базу
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for' + user)

                return redirect('login')  # переадресация на главную страничку
            else:
                print(form.errors)
        else:  # если это запрос не пост
            form = UserRegisterForm()  # Присваивание форму

        context = {'form': form}
        return render(request, 'register.html', context)



def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Имя пользователя или пароль не правильно!')

        context = {}
        return render(request, 'login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def sendhomework(request, pk):
    form = HomeworkSendForm()
    if request.method == 'POST':
        form = HomeworkSendForm(request.POST, request.FILES )
        if form.is_valid():
            das = form.save(commit=False)
            das.author = request.user
            qwe = Task.objects.get(id=pk)
            das.taskid = qwe
            das.email = request.user.email
            das.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'sendhomework.html', context)


@login_required(login_url='login')
def checkhomework(request):
    if request.user.is_teacher:
        homework = Homework.objects.all().order_by('-id')
        context = {'homework': homework}
        return render(request, 'checkhomework.html', context)
    else:
        return HttpResponse('Impossible to log')


@login_required(login_url='login')
def about(request):
    teacher = Teacher.objects.all()
    context = {'teacher': teacher}
    return render(request, 'About.html', context)


@login_required(login_url='login')
def contact(request):
    return render(request, 'Contact.html')


