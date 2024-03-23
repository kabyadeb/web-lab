from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView,DeleteView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Place
from django.contrib.auth.decorators import login_required

class HomeViewAll(ListView):
    model=Place
    template_name='home.html'
    context_object_name='places'

class HomeViewBlogs(ListView):
    model=Place
    template_name='blogs.html'
    context_object_name='places'
    def get_queryset(self):
        return Place.objects.filter(user=self.request.user).order_by('-created_at')

class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place_detail.html'  # Provide the template name where place details will be rendered
    context_object_name = 'place'

@login_required
def Createblog(request):

    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        # Assuming your form includes a file input for image
        image = request.FILES.get('image')
        print(title)
        place = Place.objects.create(
            user=request.user,
            title=title,
            description=description,
            location=location,
            image=image
        )
        
        return redirect('/') 
    else:
        return render(request, 'createblog.html')
    

class Updateblog(UpdateView):
    model=Place
    fields=['title', 'description', 'location', 'image']
    template_name='updateblog.html'
    success_url=reverse_lazy('blogs')


class Deleteblog(DeleteView):
    model=Place
    template_name='place_confirm_delete.html'
    success_url=reverse_lazy('')