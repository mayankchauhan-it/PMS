from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, "dashboard/index.html")


def add_people(request):

    if request.method == "POST":
        p_name = request.POST.get('name')
        p_number = request.POST.get('phone')
        p_type = request.POST.get('type')

        print([p_name, p_number, p_type])

        add_people = People()
        add_people.people_name = p_name
        add_people.mobile_no = p_number
        add_people.people_type = p_type

        add_people.save()

        return redirect('people_list')

    person_type = {
        'electrician' : 'Electrician',
        'mishtry' : 'Mishtry',
        'color_work' : 'Color Work'
    }

    context= {
        'parent' : 'people',
        'segment' : 'add_people',
        'person_type' : person_type,
    }

    return render(request, 'dashboard/add_people.html', context=context)

def add_building(request):

    if request.method == "POST":
        b_name = request.POST.get('building_name')
        office_number = request.POST.get('office_num')
        b_location = request.POST.get('office_location')
        b_address = request.POST.get('office_address')


        add_building = Building()
        add_building.building_name = b_name
        add_building.office_no = office_number
        add_building.location = b_location
        add_building.address = b_address

        add_building.save()

        return redirect('building_list')


    context= {
        'parent' : 'building',
        'segment' : 'add_building',
    }

    return render(request, 'dashboard/add_building.html', context=context)

def add_customer(request):

    if request.method == "POST":
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('email')
        customer_phone_no = request.POST.get('Phone_no')
        building_id = request.POST.get('building')
        people_id  = request.POST.get('people')

        building_instance = Building.objects.get(pk=building_id)
        people_instance = People.objects.get(pk=people_id)

        add_customer = Customer()
        add_customer.customer_name = customer_name
        add_customer.email = customer_email
        add_customer.phone_no = customer_phone_no

        add_customer.building = building_instance
        add_customer.resources = people_instance

        add_customer.save()

        return redirect('customer_list')

    buildings = Building.objects.all()
    people = People.objects.all()
    context= {
        'parent' : 'Customer',
        'segment' : 'add_customer',
        'buildings' : buildings,
        'people': people
    }

    return render(request, 'dashboard/add_customer.html', context=context)



def people_list(request):
    all_people = People.objects.all()

    context = {
        'parent' : 'people',
        'segment' : 'listOf_people',
        'people': all_people
    }
    return render(request, 'dashboard/list_people.html', context=context)

def building_list(request):
    all_building = Building.objects.all()

    context = {
        'parent' : 'building',
        'segment' : 'building_list',
        'buildings': all_building
    }
    return render(request, 'dashboard/list_buildings.html', context=context)

def customer_list(request):
    # to store all the objects instence of Model.
    all_customer = Customer.objects.all()

    context = {
        'parent' : 'Customer',
        'segment' : 'customer_list',
        'customers_data': all_customer
    }
    
    
    
    return render(request, 'dashboard/list_customers.html', context=context)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #





def udita_customer_list(request):
    
    all_customers = udita_Customer.objects.all()
    
    context = {
        'menuItem' : 'udita_customer',
        'submenu_name' : 'udita_customer_list',
        'customers' : all_customers
    }
    
    return render(request, 'dashboard/udita_customer_list.html', context=context)


def udita_building_list(request):
    all_building = udita_Building.objects.all()

    context = {
        'parent' : 'building',
        'segment' : 'building_list',
        'buildings': all_building
    }
    return render(request, 'dashboard/udita_building_list', context=context)
    
    
def udita_people_list(request):
    all_people = udita_People.objects.all()

    context = {
        'parent' : 'people',
        'segment' : 'listOf_people',
        'people': all_people
    }
    return render(request, 'dashboard/udita_people_list', context=context)
    