from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


# Create your views here.

# functional view
def first(request):
    return HttpResponse('Hi from view')


class Another(View):
    book = Book.objects.all()
    print(book)  # returns set
    output1 = f"We have {len(book)} books in db"
    output2 = f'first book is {book[0].title}'

    def get(self, request):
        return HttpResponse(f'{self.output1} {self.output2}')


def firstTemplate(request):
    return render(request, 'first_temp.html', {'data':'This is the data from view'})

def dynamicTemplate(request):
    books = Book.objects.all()

    return render(request, 'dynamic_template.html', {'books': books})
