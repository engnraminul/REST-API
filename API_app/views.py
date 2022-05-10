from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
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
