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
    

# from rest_framework.views import APIView

# class ContactAPIView(APIView):
#     permission_classes=[AllowAny,]
#     def post(self, request, format=None):
#         data=request.data 
#         name=data['name']
#         email=data['email']
#         phone=data['phone']
#         subject=data['subject']
#         details=data['details']

#         contact = Contact(name=name, email=email, subject=subject, phone=phone, details=details)
#         contact.save()

#         return Response({"success":"Successfully Contact is saved."})
    

#     def get(self, request, format=None):
#         return Response({"Success":"Success from Get method"})




#Model Serializer--------------

from API_app.serializers import BlogDetailsSerializer, ContactSerializer
from rest_framework.views import APIView

class ContactAPIView(APIView):
    permission_classes=[AllowAny,]
    def post(self, request, format=None):
        data=request.data 
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
       

        #return Response({"success":"Successfully Contact is saved."})
        return Response(serializer.data)
    

    def get(self, request, format=None):
        # contactobj = Contact.objects.get(id=1)
        # serializer = ContactSerializer(contactobj, many=False)
        contactobj = Contact.objects.all()
        serializer = ContactSerializer(contactobj, many=True)
        return Response(serializer.data)




#generic CreateAPIView
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from .models import Blog
from API_app.serializers import BlogSerializer
from rest_framework import status

class BlogCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        #new serializer for deatails all fields
        serializer = BlogDetailsSerializer(instance=instance, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


#CreateListAPIView (create post and return list)
class BlogListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        #new serializer for deatails all fields
        serializer = BlogDetailsSerializer(instance=instance, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BlogDetailsSerializer(queryset, many=True)
        return Response(serializer.data)





#ListAPIView
class BlogListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Blog.objects.all()
    serializer_class = BlogDetailsSerializer


