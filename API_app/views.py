from unicodedata import name
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from API_app.models import Contact

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
#@permission_classes([AllowAny])
def firstAPI(request):
    if request.method=="POST":
        name=request.data['name']
        age=request.data['age']
        print(name, age)
        return Response({"name":name, "age":age})

    context={
        'name':"MD AMINUL ISLAM",
        'University':"Green University",
    }

    return Response(context)



#Create User Login API
from django.contrib.auth.models import User
@api_view(['POST',])
def registrationAPI(request):
    if request.method=="POST":
        username=request.data['username']
        email=request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1=request.data['password1']
        password2=request.data['password2']

        if User.objects.filter(username=username).exists():
            return Response({"error":"username already exists!"})
        
        if password1 != password2:
            return Response({"error":"Password didn't matched!"})

        
        user=User()

        user.username=username
        user.email=email
        user.first_name=first_name
        user.last_name=last_name
        user.is_active=True

        user.set_password(raw_password=password1)
        user.save()

        return Response({"Success":"User Successfully Registered"})


# #Function Based API View

# @api_view(['POST',])
# def contactpost(request):
#     if request.method=="POST":
#         data=request.data 
#         name=data['name']
#         email=data['email']
#         phone=data['phone']
#         subject=data['subject']
#         details=data['details']

#         contact = Contact(name=name, email=email, subject=subject, phone=phone, details=details)
#         contact.save()

#         return Response({"success":"Successfully Contact is saved."})
    

from rest_framework.views import APIView

class ContactAPIView(APIView):
    permission_classes=[AllowAny,]
    def post(self, request, format=None):
        data=request.data 
        name=data['name']
        email=data['email']
        phone=data['phone']
        subject=data['subject']
        details=data['details']

        contact = Contact(name=name, email=email, subject=subject, phone=phone, details=details)
        contact.save()

        return Response({"success":"Successfully Contact is saved."})
    

    def get(self, request, format=None):
        return Response({"Success":"Success from Get method"})