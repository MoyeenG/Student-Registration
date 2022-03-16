from django.shortcuts import render
from .models import StudentDetail
from django.http import HttpResponse
from .stud_form import DetailsForm

# Create your views here.

def index(request):

    if request.method == 'POST':
        if request.POST.get('your_name') and request.POST.get('your_deptt') and request.POST.get('your_course'):
            obj = StudentDetail()
            my_form = DetailsForm(request.POST)
            if my_form.is_valid():
                obj.stud_name=request.POST.get('your_name')
                obj.deptt=request.POST.get('your_deptt')
                obj.course=request.POST.get('your_course')
            obj.save()
            return HttpResponse('Details Added')


    if request.method == 'GET':
        form = DetailsForm()
        name=[]
        dep=[]
        cou=[]
        for i in range(len(StudentDetail.objects.all())):
            name.append(StudentDetail.objects.all()[i].stud_name)
            dep.append(StudentDetail.objects.all()[i].deptt)
            cou.append(StudentDetail.objects.all()[i].course)
        mylist = list(zip(name, dep, cou))

        return render(request, 'index.html', {'details':mylist, 'form': form})








