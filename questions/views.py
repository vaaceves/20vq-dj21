from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Topic, Question
from .forms import LoginUserForm, SignUpUserForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView, DetailView, ListView, TemplateView, FormView
from django import template
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# Create your views here.
#
# SPANISH VIEWS
#
# index
@login_required(login_url='login_spa')
def index_spa(request):
    topic1 = Topic.objects.get(id=1)
    topic2 = Topic.objects.get(id=2)
    topic3 = Topic.objects.get(id=3)
    topic4 = Topic.objects.get(id=4)
    topic5 = Topic.objects.get(id=5)
    topics = Topic.objects.all()

    context_dic = {
        'topic1': topic1,
        'topic2': topic2,
        'topic3': topic3,
        'topic4': topic4,
        'topic5': topic5,
        'topics': topics
    }

    return render(request, 'questions/spa/index.html', context_dic)


# contact
@login_required(login_url='login_spa')
def contact_spa(request):
    topics = Topic.objects.all()

    context_dic = {
        'topics': topics
    }

    return render(request, 'questions/spa/contact.html', context_dic)


# about
@login_required(login_url='login_spa')
def about_spa(request):
    topics = Topic.objects.all()

    context_dic = {
        'topics': topics
    }

    return render(request, 'questions/spa/about.html', context_dic)


# login
class LoginUserViewSpa(View):
    login_form = LoginUserForm()
    login_error_message = None
    template = 'questions/spa/login.html'
    topics = Topic.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index_spa')
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']
        user = authenticate(username=username_post, password=password_post)
        if user is not None:
            login_django(request, user)
            return redirect('index_spa')
        else:
            self.login_error_message = "Username or Password invalid"
        return render(request, self.template, self.get_context())

    def get_context(self):
        return {
            'login_form': self.login_form,
            'login_error_message': self.login_error_message,
            'topics': self.topics
        }


# questions by topic spa
@login_required(login_url='login_spa')
def topic_spa(request, slug):
    topics = Topic.objects.all()
    context_dict = {
        'topics':topics
    }
    try:
        topic = Topic.objects.get(slug=slug)
        questions = Question.objects.filter(topic=topic)
        context_dict['topic'] = topic
        context_dict['questions'] = questions

    except Topic.DoesNotExist:
        context_dict['topic'] = None
        context_dict['questions'] = None

    return render(request, 'questions/spa/topic.html', context_dict)


# question
@login_required(login_url='login_spa')
def question_spa(request, slug):
    topics = Topic.objects.all()
    context_dict = {
        'topics': topics
    }
    try:
        question = Question.objects.get(slug=slug)
        context_dict['question'] = question

    except Topic.DoesNotExist:
        context_dict['question'] = None

    return render(request, 'questions/spa/video.html', context_dict)


# all videos
@login_required(login_url='login_spa')
def all_videos_spa(request):
    topic1 = Topic.objects.get(id=1)
    topic2 = Topic.objects.get(id=2)
    topic3 = Topic.objects.get(id=3)
    topic4 = Topic.objects.get(id=4)
    topic5 = Topic.objects.get(id=5)
    questions1 = Question.objects.filter(topic=topic1)
    questions2 = Question.objects.filter(topic=topic2)
    questions3 = Question.objects.filter(topic=topic3)
    questions4 = Question.objects.filter(topic=topic4)
    questions5 = Question.objects.filter(topic=topic5)
    topics = Topic.objects.all()

    context_dic = {
        'topic1': topic1,
        'topic2': topic2,
        'topic3': topic3,
        'topic4': topic4,
        'topic5': topic5,
        'questions1': questions1,
        'questions2': questions2,
        'questions3': questions3,
        'questions4': questions4,
        'questions5': questions5,
        'topics': topics
    }

    return render(request, 'questions/spa/all-videos.html', context_dic)


# SIGN UP
class SignUpUserViewSpa(CreateView):
    success_url = reverse_lazy('index_spa')
    template_name = 'questions/spa/signup.html'
    model = User
    form_class = SignUpUserForm

    def get(self, request, *args, **kwargs):
        context_dic = {
            'form': self.form_class,
        }
        if request.user.is_authenticated:
            return redirect('home')

        return render(request, self.template_name, context_dic)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
        self.object = authenticate(username=username, password=password)
        login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())


#
# ENGLISH VIEWS
#
# index
@login_required(login_url='login_eng')
def index_eng(request):
    topic1 = Topic.objects.get(id=1)
    topic2 = Topic.objects.get(id=2)
    topic3 = Topic.objects.get(id=3)
    topic4 = Topic.objects.get(id=4)
    topic5 = Topic.objects.get(id=5)
    topics = Topic.objects.all()

    context_dic = {
        'topic1': topic1,
        'topic2': topic2,
        'topic3': topic3,
        'topic4': topic4,
        'topic5': topic5,
        'topics': topics
    }

    return render(request, 'questions/eng/index.html', context_dic)


# contact
@login_required(login_url='login_eng')
def contact_eng(request):
    topics = Topic.objects.all()

    context_dic = {
        'topics': topics
    }

    return render(request, 'questions/eng/contact.html', context_dic)


# about
@login_required(login_url='login_eng')
def about_eng(request):
    topics = Topic.objects.all()

    context_dic = {
        'topics': topics
    }

    return render(request, 'questions/eng/about.html', context_dic)


# login
class LoginUserViewEng(View):
    login_form = LoginUserForm()
    login_error_message = None
    template = 'questions/eng/login.html'
    topics = Topic.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index_eng')
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']
        user = authenticate(username=username_post, password=password_post)
        if user is not None:
            login_django(request, user)
            return redirect('index_eng')
        else:
            self.login_error_message = "Username or Password invalid"
        return render(request, self.template, self.get_context())

    def get_context(self):
        return {
            'login_form': self.login_form,
            'login_error_message': self.login_error_message,
            'topics': self.topics
        }


# questions by topic eng
@login_required(login_url='login_eng')
def topic_eng(request, slug):
    topics = Topic.objects.all()
    context_dict = {
        'topics': topics
    }
    try:
        topic = Topic.objects.get(slug=slug)
        questions = Question.objects.filter(topic=topic)
        context_dict['topic'] = topic
        context_dict['questions'] = questions

    except Topic.DoesNotExist:
        context_dict['topic'] = None
        context_dict['questions'] = None

    return render(request, 'questions/eng/topic.html', context_dict)


# question
@login_required(login_url='login_eng')
def question_eng(request, slug):
    topics = Topic.objects.all()
    context_dict = {
        'topics': topics
    }
    try:
        question = Question.objects.get(slug=slug)
        context_dict['question'] = question

    except Topic.DoesNotExist:
        context_dict['question'] = None

    return render(request, 'questions/eng/video.html', context_dict)


# all videos
@login_required(login_url='login_eng')
def all_videos_eng(request):
    topic1 = Topic.objects.get(id=1)
    topic2 = Topic.objects.get(id=2)
    topic3 = Topic.objects.get(id=3)
    topic4 = Topic.objects.get(id=4)
    topic5 = Topic.objects.get(id=5)
    questions1 = Question.objects.filter(topic=topic1)
    questions2 = Question.objects.filter(topic=topic2)
    questions3 = Question.objects.filter(topic=topic3)
    questions4 = Question.objects.filter(topic=topic4)
    questions5 = Question.objects.filter(topic=topic5)
    topics = Topic.objects.all()

    context_dic = {
        'topic1': topic1,
        'topic2': topic2,
        'topic3': topic3,
        'topic4': topic4,
        'topic5': topic5,
        'questions1': questions1,
        'questions2': questions2,
        'questions3': questions3,
        'questions4': questions4,
        'questions5': questions5,
        'topics': topics
    }

    return render(request, 'questions/eng/all-videos.html', context_dic)


# SIGN UP
class SignUpUserViewEng(CreateView):
    success_url = reverse_lazy('index_eng')
    template_name = 'questions/eng/signup.html'
    model = User
    form_class = SignUpUserForm

    def get(self, request, *args, **kwargs):
        context_dic = {
            'form': self.form_class,
        }
        if request.user.is_authenticated:
            return redirect('home')

        return render(request, self.template_name, context_dic)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
        self.object = authenticate(username=username, password=password)
        login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())


#
# LOGOUT
#
@login_required(login_url='home')
def logout(request):
    logout_django(request)
    return redirect('index_eng')



