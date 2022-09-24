from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


def first(request):
    return HttpResponse("Testing")


def only_published_book(request):
    ''' filter will retuen list of books'''
    published_book = Book.objects.filter(is_published = True)
    return HttpResponse(published_book);

def get_only_books(request):
    book = Book.objects.get(id = 1)
    return HttpResponse(book);

class Another(View):
    books  = Book.objects.all()
    output = ''
    for book in books:
        output += "we have {} books in out database </br>".format(book.title)

    def get(self,request):
        return HttpResponse(self.output)

def rendermyhtml(request):
    return render(request,'index.html')   

def renderdynamictemplate(request):
    books = Book.objects.all();
    return render(request,'dynamic.html',{'books':books})


