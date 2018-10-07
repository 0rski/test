from django.shortcuts import render
from django.http import HttpResponse
from users.models import User

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def users(request):
    users_list = User.objects.orderby('first_name')
    user_dict = {'users': users_list}
    return render(request, 'users/index.html', context=user_dict)
