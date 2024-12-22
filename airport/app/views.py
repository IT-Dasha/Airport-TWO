from django.shortcuts import render, reverse
# Create your views here.
from django.http import HttpResponse
from django.db import connection
from .models import *
def home(request):
    return render(request, "home_page.html")
def add_plane(request):
    if 'save_plane' in request.POST:
        plane=Plane()
        plane.number_registration=request.POST.get("number_registration")
        plane.type_plane=request.POST.get("type_plane")
        plane.year_production=request.POST.get("year_production")
        plane.save(force_insert=True)
        return render(request, "add_plane.html")
    return render(request, "add_plane.html")

def add_equipage(request):
    if 'save_equipage' in request.POST:
        equipage=Equipage()
        equipage.data_formation=request.POST.get("data_formation")
        equipage.commander_equipage=request.POST.get("commander_equipage")
        equipage.save()
        return render(request, "add_equipage.html")
    return render(request, "add_equipage.html")

def add_takeoff_lane(request):
    if 'save_takeoff_lane' in request.POST:
        takeofflane=TakeoffLane()
        takeofflane.category_strips=request.POST.get("category_strips")
        takeofflane.length=request.POST.get("length")
        takeofflane.status=request.POST.get("status")
        takeofflane.save()
        return render(request, "add_takeoff_lane.html")
    return render(request, "add_takeoff_lane.html")

def add_race(request):
    plane_all=Plane.objects.all()
    equipage_all=Equipage.objects.all()
    takeofflane_all=TakeoffLane.objects.all()
    if 'save_race' in request.POST:
        race=Race()
        race.number_race=request.POST.get("number_race")
        race.date_and_time_of_departure=request.POST.get("date_and_time_of_departure")
        race.direction=request.POST.get("direction")
        race.id_plane_id=request.POST.get("id_plane_id")
        race.id_equipage_id=request.POST.get("id_equipage_id")
        race.id_takeoff_lane_id=request.POST.get("id_takeoff_lane_id")
        race.save()
        context={'plane_all':plane_all,'equipage_all':equipage_all,'takeofflane_all':takeofflane_all}
        return render(request, "add_race.html", context=context)
    context={'plane_all':plane_all,'equipage_all':equipage_all,'takeofflane_all':takeofflane_all}
    return render(request, "add_race.html", context=context)

def add_employee(request):
    equipage_all=Equipage.objects.all()
    technical_staff_all=TechnicalStaff.objects.all()
    if 'save_employee' in request.POST:
        employee=Employee()
        employee.full_name=request.POST.get("full_name")
        employee.post=request.POST.get("post")
        employee.contact_information=request.POST.get("contact_information")
        employee.id_equipage_id=request.POST.get("id_equipage_id")
        employee.id_technical_staff_id=request.POST.get("id_technical_staff_id")
        employee.save()
        context={'equipage_all':equipage_all,'technical_staff_all':technical_staff_all}
        return render(request, "add_employee.html", context=context)
    context={'equipage_all':equipage_all,'technical_staff_all':technical_staff_all}
    return render(request, "add_employee.html", context=context)


def add_technical_staff(request):
    shift_all=Shift.objects.all()
    employee_all=Employee.objects.all()
    if 'save_technical_staff' in request.POST:
        technical_staff=TechnicalStaff()
        technical_staff.education=request.POST.get("education")
        technical_staff.experience=request.POST.get("experience")
        technical_staff.id_employee_id=request.POST.get("id_employee_id")
        technical_staff.id_shift_id=request.POST.get("id_shift_id")
        technical_staff.save()
        context={'shift_all':shift_all,'employee_all':employee_all}
        return render(request, "add_technical_staff.html", context=context)
    context={'shift_all':shift_all,'employee_all':employee_all}
    return render(request, "add_technical_staff.html", context=context)


def add_flight_history(request):
    shift_all=Shift.objects.all()
    employee_all=Employee.objects.all()
    technical_staff_all=TechnicalStaff.objects.all()
    race_all=Race.objects.all()
    if 'save_flight_history' in request.POST:
        flight_history=FlightHistory()
        flight_history.id_employee_id=request.POST.get("id_employee_id")
        flight_history.id_technical_staff_id=request.POST.get("id_technical_staff_id")
        flight_history.id_shift_id=request.POST.get("id_shift_id")
        flight_history.id_race_id=request.POST.get("id_race_id")
        flight_history.save()
        context={'shift_all':shift_all,'employee_all':employee_all, 'technical_staff_all':technical_staff_all,'race_all':race_all}
        return render(request, "add_flight_history.html", context=context)
    context={'shift_all':shift_all,'employee_all':employee_all, 'technical_staff_all':technical_staff_all,'race_all':race_all}
    return render(request, "add_flight_history.html", context=context)


def all_plane(request):
    all_plane=Plane.objects.all()
    if 'delete_plane' in request.POST:
        all_plane=Plane.objects.all()
        id=request.POST.get("id_plane")
        delete_plane=Plane.objects.filter(id_plane=id)
        delete_plane.delete()
        context={'all_plane':all_plane}
        return render(request, "all_plane.html", context=context)
    if 'update_plane' in request.POST:
        all_plane=Plane.objects.all()
        plane=Plane()
        plane.id_plane=request.POST.get("id_plane")
        plane.number_registration=request.POST.get("number_registration")
        plane.type_plane=request.POST.get("type_plane")
        plane.year_production=request.POST.get("year_production")
        plane.save(force_update=True)
        print(plane.id_plane)
        context={'all_plane':all_plane}
        return render(request, "all_plane.html", context=context)
    context={'all_plane':all_plane}
    return render(request, "all_plane.html", context=context)



def all_employee(request):
    all_employee=Employee.objects.all()
    all_equipage=Equipage.objects.all()
    all_technical_staff=TechnicalStaff.objects.all()
    if 'delete_employee' in request.POST:
        all_equipage=Equipage.objects.all()
        all_technical_staff=TechnicalStaff.objects.all()
        all_employee=Employee.objects.all()
        id=request.POST.get("id_employee")
        delete_employee=Employee.objects.filter(id_employee=id)
        delete_employee.delete()
        context={'all_employee':all_employee,'all_equipage':all_equipage,'all_technical_staff':all_technical_staff}
        return render(request, "all_employee.html", context=context)
    if 'update_employee' in request.POST:
        all_employee=Employee.objects.all()
        all_equipage=Equipage.objects.all()
        all_technical_staff=TechnicalStaff.objects.all()
        all_technical_staff=TechnicalStaff.objects.all()
        employee=Employee()
        qwe=request.POST.get("id_employee")
        employee.id_employee=request.POST.get("id_employee")
        employee.full_name=request.POST.get("full_name")
        employee.post=request.POST.get("post")
        employee.contact_information=request.POST.get("contact_information")
        employee.id_equipage_id=request.POST.get("id_equipage")
        employee.id_technical_staff_id=request.POST.get("id_technical_staff")
        employee.save(force_update=True)
        context={'all_employee':all_employee,'all_equipage':all_equipage,'all_technical_staff':all_technical_staff}
        all_equipage=Equipage.objects.all()
        return render(request, "all_employee.html", context=context)
    context={'all_employee':all_employee,'all_equipage':all_equipage,'all_technical_staff':all_technical_staff}
    return render(request, "all_employee.html", context=context)

def all_equipage(request):
    all_equipage=Equipage.objects.all()
    if 'delete_equipage' in request.POST:
        all_equipage=Equipage.objects.all()
        id=request.POST.get("id_equipage")
        delete_equipage=Equipage.objects.filter(id_equipage=id)
        delete_equipage.delete()
        context={'all_equipage':all_equipage}
        return render(request, "all_equipage.html", context=context)
    if 'update_equipage' in request.POST:
        all_equipage=Equipage.objects.all()
        equipage=Equipage()
        equipage.id_equipage=request.POST.get("id_equipage")
        equipage.data_formation=request.POST.get("data_formation")
        equipage.commander_equipage=request.POST.get("commander_equipage")
        equipage.save(force_update=True)
        context={'all_equipage':all_equipage}
        return render(request, "all_equipage.html", context=context)
    context={'all_equipage':all_equipage}
    return render(request, "all_equipage.html", context=context)


def all_technical_staff(request):
    all_technical_staff=TechnicalStaff.objects.all()
    all_employee = Employee.objects.all()
    all_shift = Shift.objects.all()
    if 'delete_technical_staff' in request.POST:
        all_employee = Employee.objects.all()
        all_shift = Shift.objects.all()
        all_technical_staff=TechnicalStaff.objects.all()
        id=request.POST.get("id_technical_staff")
        delete_technical_staff=TechnicalStaff.objects.filter(id_technical_staff=id)
        delete_technical_staff.delete()
        context={'all_technical_staff':all_technical_staff, 'all_employee':all_employee, 'all_shift':all_shift}
        return render(request, "all_technical_staff.html", context=context)
    if 'update_technical_staff' in request.POST:
        all_employee = Employee.objects.all()
        all_shift = Shift.objects.all()
        all_technical_staff=TechnicalStaff.objects.all()
        technical_staff=TechnicalStaff()
        technical_staff.id_technical_staff=request.POST.get("id_technical_staff")
        technical_staff.education=request.POST.get("education")
        technical_staff.experience=request.POST.get("experience")
        technical_staff.id_employee_id=request.POST.get("id_employee")
        technical_staff.id_shift_id=request.POST.get("id_shift")
        technical_staff.save(force_update=True)
        context={'all_technical_staff':all_technical_staff, 'all_employee':all_employee, 'all_shift':all_shift}
        return render(request, "all_technical_staff.html", context=context)
    return render(request, "all_technical_staff.html", context={'all_technical_staff':all_technical_staff, 'all_employee':all_employee, 'all_shift':all_shift})

def all_race(request):
    all_race=Race.objects.all()
    all_plane=Plane.objects.all()
    all_equipage=Equipage.objects.all()
    all_takeofflane=TakeoffLane.objects.all()
    if 'delete_race' in request.POST:
        all_race=Race.objects.all()
        all_plane=Plane.objects.all()
        all_takeofflane=TakeoffLane.objects.all()
        id=request.POST.get("id_race")
        delete_race=Race.objects.filter(id_race=id)
        delete_race.delete()
        context={'all_race':all_race, all_plane:'all_plane', 'all_equipage':all_equipage, 'all_takeofflane':all_takeofflane}
        return render(request, "all_race.html", context=context)
    if 'update_race' in request.POST:
        all_race=Race.objects.all()
        all_plane=Plane.objects.all()
        all_equipage=Equipage.objects.all()
        all_takeofflane=TakeoffLane.objects.all()
        race=Race()
        race.id_race=request.POST.get("id_race")
        race.number_race=request.POST.get("number_race")
        race.date_and_time_of_departure=request.POST.get("date_and_time_of_departure")
        race.direction=request.POST.get("direction")
        race.id_plane_id=request.POST.get("id_plane")
        race.id_equipage_id=request.POST.get("id_equipage")
        race.id_takeoff_lane_id=request.POST.get("id_takeoff_lane")
        race.save(force_update=True)
        context={'all_race':all_race, 'all_plane':all_plane, 'all_equipage':all_equipage, 'all_takeofflane':all_takeofflane}
        return render(request, "all_race.html", context=context)
    context={'all_race':all_race, 'all_plane':all_plane, 'all_equipage':all_equipage, 'all_takeofflane':all_takeofflane}
    return render(request, "all_race.html", context=context)


def all_shift(request):
    all_shift=Shift.objects.all()
    if 'delete_shift' in request.POST:
        all_shift=Shift.objects.all()
        id=request.POST.get("id_shift")
        delete_shift=Shift.objects.filter(id_shift=id)
        delete_shift.delete()
        context={'all_shift':all_shift}
        return render(request, "all_shift.html", context=context)
    if 'update_shift' in request.POST:
        all_shift=Shift.objects.all()
        shift=Shift()
        shift.id_shift_id=request.POST.get("id_shift")
        shift.time_start=request.POST.get("time_start")
        shift.time_end=request.POST.get("time_end")
        shift.save(force_update=True)
        context={'all_shift':all_shift}
        return render(request, "all_shift.html", context=context)
    context={'all_shift':all_shift}
    return render(request, "all_shift.html", context=context)


def all_takeofflane(request):
    all_takeofflane=TakeoffLane.objects.all()
    if 'delete_takeofflane' in request.POST:
        all_takeofflane=TakeoffLane.objects.all()
        id=request.POST.get("id_takeoff_lane")
        delete_takeofflane=TakeoffLane.objects.filter(id_takeoff_lane=id)
        delete_takeofflane.delete()
        context={'all_takeofflane':all_takeofflane}
        return render(request, "all_takeofflane.html", context=context)
    if 'update_takeofflane' in request.POST:
        all_takeofflane=TakeoffLane.objects.all()
        takeofflane=TakeoffLane()
        takeofflane.id_takeoff_lane=request.POST.get("id_takeoff_lane")
        takeofflane.category_strips=request.POST.get("category_strips")
        takeofflane.length=request.POST.get("length")
        takeofflane.status=request.POST.get("status")
        takeofflane.save(force_update=True)
        context={'all_takeofflane':all_takeofflane}
        return render(request, "all_takeofflane.html", context=context)
    context={'all_takeofflane':all_takeofflane}
    return render(request, "all_takeofflane.html", context=context)

def all_flight_history(request):
    all_flight_history=FlightHistory.objects.all()
    all_employee=Employee.objects.all()
    all_technical_staff=TechnicalStaff.objects.all()
    all_shift=Shift.objects.all()
    all_race = Race.objects.all()
    if 'delete_flight_history' in request.POST:
        all_flight_history=FlightHistory.objects.all()
        all_employee=Employee.objects.all()
        all_technical_staff=TechnicalStaff.objects.all()
        all_shift=Shift.objects.all()
        all_race = Race.objects.all()
        id=request.POST.get("id_flight_history")
        delete_flight_history=FlightHistory.objects.filter(id=id)
        delete_flight_history.delete()
        context={'all_flight_history':all_flight_history, 'all_employee':all_employee, 'all_technical_staff':all_technical_staff, 'all_shift':all_shift, 'all_race':all_race}
        return render(request, "all_flight_history.html", context=context)
    if 'update_flight_history' in request.POST:
        all_flight_history=FlightHistory.objects.all()
        all_employee=Employee.objects.all()
        all_technical_staff=TechnicalStaff.objects.all()
        all_shift=Shift.objects.all()
        all_race = Race.objects.all()
        flight_history=FlightHistory()
        flight_history.id_flight_history=request.POST.get("id_flight_history")
        flight_history.id_employee_id=request.POST.get("id_employee")
        flight_history.id_technical_staff_id=request.POST.get("id_technical_staff")
        flight_history.id_shift_id=request.POST.get("id_shift")
        flight_history.id_race_id=request.POST.get("id_race")
        flight_history.save(force_update=True)
        context={'all_flight_history':all_flight_history, 'all_employee':all_employee, 'all_technical_staff':all_technical_staff, 'all_shift':all_shift, 'all_race':all_race}
        return render(request, "all_flight_history.html", context=context)
    context={'all_flight_history':all_flight_history, 'all_employee':all_employee, 'all_technical_staff':all_technical_staff, 'all_shift':all_shift, 'all_race':all_race}
    return render(request, "all_flight_history.html", context=context)


def home_employee(request):
    return render(request, "home_page_employes.html")


from django.db import connection, DatabaseError

def post(request):
        if 'but' in request.POST:
            post = request.POST.get("post")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows':rows}
            return render(request, "post.html",context=context)
        else:
            return render(request, "post.html")
        

def postes(request):
        if 'but_0_1' in request.POST:
            post = request.POST.get("post_0_1")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_0_1':rows}
            return render(request, "postes.html",context=context) 
        if 'but_0_2' in request.POST:
            post = request.POST.get("post_0_2")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_0_2':rows}
            return render(request, "postes.html",context=context)        
        if 'but_0_3' in request.POST:
            post = request.POST.get("post_0_3")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_0_3':rows}
            return render(request, "postes.html",context=context)
        if 'but_1' in request.POST:
            post = request.POST.get("post_1")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_1':rows}
            return render(request, "postes.html",context=context)
        if 'but_2' in request.POST:
            post = request.POST.get("post_2")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_2':rows}
            return render(request, "postes.html",context=context)
        if 'but_3' in request.POST:
            post = request.POST.get("post_3")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_3':rows}
            return render(request, "postes.html",context=context)
        if 'but_4' in request.POST:
            post = request.POST.get("post_4")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_4':rows}
            return render(request, "postes.html",context=context)
        if 'but_5' in request.POST:
            post = request.POST.get("post_5")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_5':rows}
            return render(request, "postes.html",context=context)
        if 'but_6' in request.POST:
            post = request.POST.get("post_6")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_6':rows}
            return render(request, "postes.html",context=context)
        if 'but_7' in request.POST:
            post = request.POST.get("post_7")
            with connection.cursor() as cursor:
                cursor.execute(post)
                rows = cursor.fetchall()  # Получаем все строки
                print(rows)
                context = {'rows_7':rows}
            return render(request, "postes.html",context=context)
        else:
            return render(request, "postes.html")

