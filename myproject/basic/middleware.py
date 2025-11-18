from django.http import JsonResponse
import re,json

class basicMiddleware:
    def __init__(self, get_response):    #whenever we start the server
        self.get_response = get_response

    def __call__(self, request):          #whenever we make a request
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request,"hello")
        if (request.path == 'add/'):
          print(request.method,"method")
          print(request.path)
        response = self.get_response(request)
        return response


# class signupMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         data=json.loads(request.body)
#         username=data.get("username")
#         email=data.get("email")
#         dob=data.get("dob")
#         password=data.get("pswd")
        #check username rules with Regex
        #check email rules with regex
        #check dob rules with regex
        #check password rules with regex
        
class SscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ["/job1/","/job2/"]):
            ssc_result=request.GET.get("ssc")  #params it means it will take from postman url which we give and store in sscresults
            print(ssc_result,'hello')
            if(ssc_result !='True'):
                return  JsonResponse({"error":"u should qualify atleast ssc for applying this job"},status=400)
        return self.get_response(request)

 
class MedicalFitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path == "/job1/"):
            medical_fit_result=request.GET.get("medically_fit")
            if(medical_fit_result !='True'):
                return JsonResponse({"error":"u not medically fit to apply for this job role"},status=400)
        return self.get_response(request)
 
class AgeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path in ["/job1/","/job2/"]):
            Age_checker=int(request.GET.get("age",17))
            if Age_checker >25 or Age_checker<18 :
                return JsonResponse({"error":"age must be in b/w 18 and 25"},status=400)
        return self.get_response(request)
    
class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/signup/"):
            data=json.loads(request.body)
            username=data.get("username")
            #checks username is empty or not
            if not username:
                return JsonResponse({"error":"username is required"},status=400)
            if len(username)<3 or len(username)>20:
                return JsonResponse({"error":"username should contains 2 to 20 characters"},status=400)
            if username[0] in "._" or username[-1] in "._":
                return JsonResponse({"error":"username should not starts/ends with . or _ "},status=400)
            if not re.match(r"^[a-zA-Z0-9._]+$",username):
                return JsonResponse({"error":"username should contains only letters,numbers,dot,underscore"},status=400)
            if ".." in username or "__" in username:
                return JsonResponse({"error":"sholud not have .. or __ "},status=400)
        
        return self.get_response(request)
