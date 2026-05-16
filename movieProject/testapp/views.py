from django.shortcuts import render, redirect
from testapp.models import Movie
from testapp.forms import MovieForm
# Create your views here.

# USER ==> URL ==> VIEWS ==> TEMP ==> (OUTPUT)
def home_view(request):  # Home View
    return render(request, 'testapp/index.html')

def add_view(request):  # Add View
    form = MovieForm() # Create form object
    
    if request.method == 'POST':  # True
        form = MovieForm(request.POST) 
        if form.is_valid():   # CSRF
            form.save(commit=True)
        # return display_view(request)
        return redirect('display')
    return render(request, 'testapp/add.html', {'form':form})



def display_view(request):  # Display View
    movie_list = Movie.objects.all()
    return render(request, 'testapp/display.html', {'movie_list':movie_list})