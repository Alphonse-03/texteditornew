from django.shortcuts import render
from django.http import HttpResponse
def home(request):

    return render(request,"a.html")


def analyze(request):
    text = request.POST.get("text","default")
    space=request.POST.get("space","off")
    punct=request.POST.get("punctuations","off")
    nline=request.POST.get("line","off")
    cap=request.POST.get("cap","off")
    rnum=request.POST.get("rnum","off")
    newtext=""
    if(space=="on"):
        newtext=""
        for i,char in enumerate(text):
            if(i==0):
                i=1
            if not(text[i-1] == " " and text[i] == " "):
                 newtext = newtext + char
             

    #params={"text":newtext}
        text=newtext
    if punct=="on":
        newtext=""
        punc='''!@#$%^&*()_"':;?/.,~`'''
        for char in text:
           if char not in punc:
                newtext=newtext+char 
       
    #    params={"text":newtext}
        text=newtext

    if rnum=="on":
        newtext=""
        num='0123456789'
        for char in text:
           if char not in num:
                newtext=newtext+char 
      
        #params={"text":newtext}
        text=newtext
    if cap=="on":
        newtext=""
        for char in text:
            newtext=newtext+char.upper() 
        #params={"text":newtext}
        text=newtext
    if nline=="on":
        newtext=""
        for char in text:
           if char != "\n" and char!="\r":
                newtext=newtext+char 
        #params={"text":newtext}
        text=newtext
    return render(request,"space.html",{"text":newtext})
    
def about(request):
    return render(request,"about.html")
