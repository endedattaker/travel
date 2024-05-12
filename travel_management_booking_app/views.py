from django.shortcuts import render,redirect
from .models import Packages , Booking
from.forms import Bookingform

# Create your views here.


def packages(request):
    x=Packages.objects.all()
    mydict={'x':x}
    return render (request,'packages.html',context=mydict)

def booking(request):
    if request.method=='POST':
        form=Bookingform(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/travel_management_app/success/')
    else:
        form=Bookingform()
    return render(request,'booking.html',{'forms':form})





