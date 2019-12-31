from django.shortcuts import render
# from django.http import HttpResponse
from eica.models import Personas

# Formularios
from eica.forms import PersonasForm


def homepage_view(request, *args, **kwargs):
    # return HttpResponse("Home")
    return render(request,'home.html',{})

def table_view(request):
    personas = Personas.objects.all()
    return render(request,'table.html',locals())    


def apinuevo(request):
    personas = Personas.objects.all()
    
    if request.method=='POST':
        form=PersonasForm(request.POST)
        if form.is_valid():
            form.save()
        # return redirect('apinuevo:apinuevo')
    else:
        form=PersonasForm()
    
    return render(request,'apinuevo.html',{'p':personas,'form':form})    

