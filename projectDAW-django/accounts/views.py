from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .controller import ListarServicio,ListarCita, Add
from django.utils.dateparse import parse_date
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            listaservicio = ListarServicio('servicios')
            context = {'service': listaservicio}
            return render(request, 'userprofile.html', context)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def userprofile(request):
    listaservicio = ListarServicio('servicios')
    context = {'service': listaservicio}
    return render(request, 'services.html', context)


def ListarCitas(request):
    listacitas = ListarCita('cita')
    context = {'cita':listacitas}
    return render(request, 'horarios.html', context) 


def add(request):
    if request.method == 'POST':
        registro = {'date':request.POST.get('date'), 'service': request.POST.get('sevice'), 'id_user': request.POST.get('id_user')}
        Add(registro)
        return redirect('userprofile')
    else: 
        return render(request,'add-appo.html')

