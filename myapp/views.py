from django.shortcuts import render,redirect

from django.contrib import messages

from django.views.generic import View

from myapp.forms import EmployeeForm

from myapp.models import Employees

# Create your views here.

class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        return render(request,"employe_create.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)  

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employees.objects.create(**data)

            messages.success(request,"added succssfully")
            
            return redirect('employe_list')

        else:

            messages.error(request,"added failed")

            return render(request,"employe_create.html",{"form":form_instance})



class EmployeListView(View):

        def get(self,request,*args,**kwargs):            

            qs=Employees.objects.all()

            return render(request,"employe_list.html",{"employe":qs})


class EmployeDetailsView(View):

        def get(self,request,*args,**kwargs): 

            id=kwargs.get("pk")

            qs=Employees.objects.get(id=id)

            return render(request,"employe_details.html",{"employe":qs})


class EmployeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employees.objects.get(id=id).delete()

        messages.error(request,"deleted successfully ")

        return redirect("employe_list")


class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        emp_obj=Employees.objects.get(id=id)

        emp_dict={
            "name":emp_obj.name,
            "designation":emp_obj.designation,
            "department":emp_obj.department,
            "salary":emp_obj.salary,
            "contact":emp_obj.contact,
            "address":emp_obj.address,

        }

        form_instance=EmployeeForm(initial=emp_dict)

        return render(request,"employe_update.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Employees.objects.filter(id=id).update(**data)

            messages.success(request,"updated successfully")

            return redirect("employe_list") 

        else:

            messages.error(request,"update failed")

            return render(request,"employe_update.html",{"form":form_instance})


            
   
