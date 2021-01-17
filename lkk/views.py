from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ZayavkaForm, Zayavitel_yur, Zayavitel_people
from .models import People
from django.shortcuts import redirect
from django.utils import timezone



# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def zayavka_new(request):
    if request.method == "POST":
        form = ZayavkaForm(request.POST)
        if form.is_valid():
            zayavka = form.save(commit=False)
            zayavka.author = request.user
            zayavka.created_date = timezone.now()
            zayavka.save()
            return redirect('zayavka_detail', pk=zayavka.pk)
    else:
        form = ZayavkaForm()
    return render(request, 'lkk/zayavka_new.html', {'form': form})

def profile_ur(request):
    if request.method == "POST":
        form1 = Zayavitel_yur(request.POST)
        form2 = Zayavitel_people(request.POST)
        if form1.is_valid() and form2.is_valid():
            zayavitel1 = form1.save(commit=False)
            zayavitel2 = form2.save(commit=False)
            zayavitel1.author = request.user
            zayavitel1.created_date = timezone.now()
            zayavitel1.fio = zayavitel2.pk
            zayavitel1.save()
            return redirect('zayavka_detail', pk=zayavitel1.pk)
    else:
        form1 = Zayavitel_yur()
        form2 = Zayavitel_people()
    return render(request, 'lkk/profile.html', {'form1': form1, 'form2': form2, 'title': 'Редактирование'})

#@login_required
def profile(request, step):
    if step == 1 :
        try:
            people1 = People.objects.get(author=request.user)
            people_nayden = True
        except People.DoesNotExist:
            people_nayden = False
        #people1 = get_object_or_404(People, author=request.user)
        if request.method == "POST":
            if people_nayden:
                form = Zayavitel_people(request.POST, instance=people1)
            else:
                form = Zayavitel_people(request.POST)
            if form.is_valid():
                people = form.save(commit=False)
                people.author = request.user
                people.created_date = timezone.now()
                people.save()
                return redirect('/lk/profile/2')
        else:
            if people_nayden:
                form = Zayavitel_people(instance=people1)
            else:
                form = Zayavitel_people()
        return render(request, 'lkk/profile_step.html', {'form': form, 'title': 'Данные о заявителе'})
    elif step == 2:
        if request.method == "POST":
            form = Zayavitel_yur(request.POST)
            if form.is_valid():
                people = form.save(commit=False)
                people.author = request.user
                people.created_date = timezone.now()
                people.save()
                return redirect('profile', step=3)
        else:
            form = Zayavitel_yur()
            form.fields['fio'] = People.objects.get(author=request.user)
        return render(request, 'lkk/profile_step.html', {'form': form, 'title': 'Данные об организации'})

def profile_view(request):
        fio = People.objects.filter(author=request.user)
        return render(request, 'lkk/profile_view.html', {'fio': fio, 'title' : 'Персоны'})


def profile_edit(request, pkk):
    try:
        people1 = People.objects.get(pk=pkk, author=request.user)
        people_nayden = True
    except People.DoesNotExist:
        people_nayden = False
    #people1 = get_object_or_404(People, author=request.user)
    if request.method == "POST":
        if people_nayden:
            form = Zayavitel_people(request.POST, request.FILES, instance=people1)
        else:
            form = Zayavitel_people(request.POST, request.FILES)
        if form.is_valid():
            people = form.save(commit=False)
            #people.doc_polnomochia = People(request.FILES['doc_polnomochia'])
            people.author = request.user
            people.created_date = timezone.now()
            people.save()
            return redirect('person')
    else:
        if people_nayden:
            form = Zayavitel_people(instance=people1)
        else:
            form = Zayavitel_people()
    return render(request, 'lkk/profile_step.html', {'form': form, 'title': 'Данные о персонах'})