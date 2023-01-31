from django.http import HttpResponse
from django.shortcuts import render
from.models import place
# Create your views here.


def mywork(request):
    obj=place.objects.all()
    return render(request,'index.html',{'result':obj})












#def home(request):
 #   return HttpResponse("This is home")

#def addition(request):
    #x = int(request.GET['no1'])
    #y = int(request.GET['no2'])
    #a = x + y
    #s = x - y
    #m = x * y
    #d = x / y
    #return render(request,'result.html',{'ans1':a,'ans2':s,'ans3':m,'ans4':d})

#def about(request):
 #   return  render(request,'about.html')

#def contact(request):
 #   return render(request,'contact.html')

#def details(request):
 #   return  HttpResponse("These are details")

#def thanks(request):
 #   return render(request,'thanks.html')
