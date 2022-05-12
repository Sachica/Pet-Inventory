from django.shortcuts import render
from django import views
from .models import User
# Create your views here.


class index(views.View):

    def get(self, request):
        return render(request, 'users/index.html')
    


class iniciarSesion(views.View):
    
    def get(self, request):
        return render(request, 'users/iniciarSesion.html')
    
    def post(self, request):
        print(request.POST)
        email = request.POST['txtEmail']
        password = request.POST['txtPassword']
        user = User.objects.filter(email=email, password=password).first()
        print(user)

        if user is None :
            return render(request, 'users/index.html')
        else :
            
             return render(request, 'pets/dashboard.html')