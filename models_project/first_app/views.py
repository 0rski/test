from django.shortcuts import render

# Create your views here.
def index(request):
    first_app_dir = {"title_h2": "I'm the inserted title", }
    return render(request, 'first_app/index.html', context=first_app_dir)
# def help(request):
#     help_dictionary = {'insert_var' : "i added succesfully"}
#     return render(request, 'help/index.html', context=help_dictionary)
