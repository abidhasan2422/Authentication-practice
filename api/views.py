
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny,IsAuthenticated,IsAdminUser


class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,*args, **kwargs):
        return self.list(request, *args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args, **kwargs)

class UDRStudentAPI(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
     queryset = Student.objects.all()
     serializer_class= StudentSerializer
     authentication_classes=[SessionAuthentication]
     permission_classes=[IsAuthenticatedOrReadOnly]

     def get(self,request,*args, **kwargs):
         return self.retrieve(request,*args, **kwargs)
     def put(self,request,*args, **kwargs):
         return self.update(request,*args, **kwargs)
     def delete(self,request,*args, **kwargs):
         return self.destroy(request, *args, **kwargs)
    

