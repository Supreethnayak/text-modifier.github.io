#I have created this file - Supreeth
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Harry</h1> <a href="https://www.w3schools.com/sql/" target="_blank"> W3schools</a> <br>
#     <a href="https://prepinsta.com/top-100-codes/" target="_blank"> prep</a> <br>
#     <a href="https://www.tutorialspoint.com/django/django_creating_project.htm" target="_blank"> tutorialspoint</a> <br>
#     <a href="https://github.com/hiteshchoudhary/DjangoExercise1" target="_blank"> lco</a>''')
#
# def about(request):
#     return HttpResponse("About Harry Bhai")

# view returns http response
def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home")

def ex1(request):
     return HttpResponse('''<h1>Harry</h1> <a href="https://www.w3schools.com/sql/" target="_blank"> W3schools</a> <br>
    <a href="https://prepinsta.com/top-100-codes/" target="_blank"> prep</a> <br>
    <a href="https://www.tutorialspoint.com/django/django_creating_project.htm" target="_blank"> tutorialspoint</a> <br>
    <a href="https://github.com/hiteshchoudhary/DjangoExercise1" target="_blank"> lco</a>''')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')
    # print(djtext)

    #Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')

    # print(removepunc)
    # print(djtext)

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        #iterating through inputed text
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed the NewLines','analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Removed the Extra spaces','analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if charcounter == "on":
        count = 0
        for char in djtext:
            count = count + 1
        params = {'purpose':'Charector Count is','analyzed_text': count}
        # djtext = analyzed
        # return render(request,'analyze.html',params)

    # else:
    #     return HttpResponse("Error")

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request,'analyze.html',params)

# def capfirst(request):
#     return HttpResponse('''capitalize first <br> <a href="/">back</a>''')
#
# def newlineremove(request):
#     return HttpResponse('''newline remover <br> <a href="/">back</a>''')
#
# def spaceremove(request):
#     return HttpResponse('''space remover <br> <a href="/">back</a>''')
#
# def charcount(request):
#     return HttpResponse('''char counter <br> <a href="/">back</a>''')
