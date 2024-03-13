from django.shortcuts import render
from composeapp.models import studentdata
# Create your views here.f
def studentform(request):
    if request.method == "GET":
        return render (request,'student.html')
    
    
    else:
        studentdata(
            first_name=request.POST.get('first'),
            last_name=request.POST.get('last')
        ).save()
        print("Data insert into database")
        return render(request,'student.html')