from django.shortcuts import render, redirect
from .models import*
from django.contrib import messages

def index(request):
    all_books = Books.objects.all()
    context ={
        'books':all_books
    }
    return render(request,'index.htm',context)

def createBook(request):
    # print(request.POST)
    # this is the function we want to validate b/c it is the route from the form on HTML
    errors = Books.objects.bookValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    newBook = Books.objects.create(title= request.POST['form_title'], desc= request.POST['form_desc'])
    return redirect("/")

def showBook(request, bookid):
    bookShow = Books.objects.get(id= bookid)
    context ={
        'bookBook': bookShow,
        'allAuthors': Authors.objects.all(),
    }
    return render(request, "books.htm",context)

def addAuthorToBook(request, bookid):
    print(request.POST)
    this_author= Authors.objects.get(id= int(request.POST['author']))
    this_book= Books.objects.get(id= bookid)

    this_author.books.add(this_book)
    return redirect(f"/books/{bookid}")

def deleteBook(request, bookid):
    b = Books.objects.get(id=bookid)
    b.delete()
    return redirect('/')

def editBook(request, bookid):
    context ={
        'bookToGet': Books.objects.get(id=bookid)
    }

    return render(request, 'edit.htm',context)

def updateBook(request, bookid):
    # print(request.POST)
    b = Books.objects.get(id=bookid)
    b.title=request.POST['form_title']
    b.desc=request.POST['form_desc']
    b.save()
    return redirect("/")