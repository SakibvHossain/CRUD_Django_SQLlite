from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookCreate
#from django.contrib import messages


# def stdisplay(request):
#     result = Book.objects.all()
#     return render(request,'upload_form.html',{'Book':result})

# def stinsert(request):
#     if request.method == 'POST':
#         if request.POST.get('player_name1') and request.POST.get('player_email1') and  request.POST.get('player_role1') and request.POST.get('team_logo1') and  request.POST.get('game_name1') and request.POST.get('team_code1'):
#             savest = Book()
#             savest.player_name = request.POST.get('player_name')
#             savest.player_email = request.POST.get('player_email1')
#             savest.team_role = request.POST.get('player_role1')
#             savest.team_logo = request.POST.get('team_logo1')
#             savest.game_name = request.POST.get('game_name1')
#             savest.team_code = request.POST.get('team_code1')
#             savest.save()
#             messages.success(request, "The record "+savest.player_name+"Is Saved Successfully..!")
#             return render(request, "team_create.html")
#     else:
#         return render(request, "team_create.html")




def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/team_create.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index') 
        else:
            return HttpResponse(""" Something went wrong. Please reload  Click here <a href="{{url:'index'}}"> Reload </a> """)
    
    else:
        return render(request, 'book/upload_form.html', {'upload_form': upload})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form': book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_shelf.delete()
    return redirect('index')
