from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import StudentNew,Users


# Create your views here.

def sample(request):
    return HttpResponse('hi')
def sample1(request):
    return HttpResponse('My Name is Sai Amruth')
def sample2(request):
    data={"name":"saiamruth","age":25,"place":"hyd"}
    return JsonResponse(data)
def sample3(request):
    data={"result":[2,4,6,8]}
    return JsonResponse(data)
def dynamic(request):
    name=request.GET.get("name",'')
    city=request.GET.get("city",'hyd')
    return HttpResponse(f"{name} from {city}")
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"OK","db":"Connected"})
    except Exception as e:
        return JsonResponse({"status":"Error","db":str(e)})

#CRUD operations using HTTP methods(post,get,put,delete) 
@csrf_exempt
def addStudent(request):
    if request.method=='POST':
        data=json.loads(request.body)
        student=StudentNew.objects.create(
            name=data.get('name'),
            age=data.get('age'),
            email=data.get('email')
            )
        return JsonResponse({"status":"success","id":student.id},status=200)
    
#------------------------------------
    elif request.method=='GET':
        result=list(StudentNew.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)

#--------------------------------------------
    #task Codes----
    # elif request.method == 'GET':
    #     student_id = request.GET.get('id')  # <-- get 'id' from URL query parameter

    #     if student_id:
    #         try:
    #             student = StudentNew.objects.get(id=student_id)
    #             result = {
    #             'id': student.id,
    #             'name': student.name,
    #             'age': student.age,
    #             'email': student.email
    #         }
    #             return JsonResponse({"status": "OK", "data": result}, status=200)
    #         except StudentNew.DoesNotExist:
    #             return JsonResponse({"error": "Student not found"}, status=404)
    #     else:
    #     # If no ID is provided, return all students
    #         result = list(StudentNew.objects.values())
    #         return JsonResponse({"status": "OK", "data": result}, status=200)

    
#--------------------------------------------------------
    elif request.method=='PUT':
        data=json.loads(request.body)
        ref_id=data.get('id')  #getting id
        new_email=data.get('email') #getting email
        existing_student=StudentNew.objects.get(id=ref_id) #fetched the object as per the id

        existing_student.email=new_email #updating with new email
        existing_student.save() #upto here is enough line no 59,60 optional not mandatory
        updated_data=StudentNew.objects.filter(id=ref_id).values().first()
        return JsonResponse({"status":"data updated successfully","updated_data":updated_data},status=200)
    
#-------------------------------------------------------
    elif request.method=='DELETE':
        data=json.loads(request.body)
        ref_id=data.get('id')  #getting id
        get_deleting_data=StudentNew.objects.filter(id=ref_id).values().first()
        to_be_delete=StudentNew.objects.get(id=ref_id)
        to_be_delete.delete()

        return JsonResponse({"status":"sucess","message":"Student data deleted sucessfully","get deleted data":get_deleting_data},status=200)
    return JsonResponse({"error":"Something Went Wrong, Check Code Correctly!"},status=400)


def job1(request):
    return JsonResponse({"message":"You have successfully applied for job1"},status=200) 
def job2(request):
    return JsonResponse({"message":"You have successfully applied for job2"},status=200)

@csrf_exempt   
def signup(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        user=Users.objects.create(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
            )
        return JsonResponse({"data":"success"},status=200)