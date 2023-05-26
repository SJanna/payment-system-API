from rest_framework import generics
from django.http import HttpResponse
from .models import Payment
from django.contrib.auth.models import User
from payments.permisions import IsOwner
from .serializers import PaymentSerializer

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Payment.objects.all()
        elif user.is_authenticated:
            return Payment.objects.filter(user=user.id)
        return User.objects.none()
    
def ok_view(request):
    content = "OK"
    response = HttpResponse(content, status=200)
    return response

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list` and `retrieve` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsOwner]

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_superuser:
#             return User.objects.all()
#         elif user.is_authenticated:
#             return User.objects.filter(id=user.id)
#         return User.objects.none()
    



        