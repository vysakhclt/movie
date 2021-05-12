from django.http import HttpResponse
# from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from .models import movie
from .forms import movieForm


# Create your views here.
def index(request):
    movies = movie.objects.all()
    context = {
        'movie_list': movies
    }
    return render(request, "index.html", context)


def details(request, movie_id):
    Movie = movie.objects.get(id=movie_id)
    return render(request, "details.html", {'Movie': Movie})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image = request.FILES['image']
        M = movie(name=name, desc=desc, year=year, image=image)
        M.save()
    return render(request, 'add.html')


def update(request, id):  # for same id
    mov = movie.objects.get(id=id)
    form = movieForm(request.POST or None, request.FILES, instance=mov)  # passing to mov variable
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'mov': mov})


def delete(request, id):
    if request.method == "POST":
        mov = movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request, 'delete.html')
