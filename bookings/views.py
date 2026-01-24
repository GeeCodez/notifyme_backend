import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from .tasks import send_booking_email

from .models import Booking
from .serializers import BookingSerializer

class BookingCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        booking = Booking.objects.create(
            user=request.user,
            reference=str(uuid.uuid4())
        )

        send_booking_email.delay(
            request.user.email,
            booking.reference
        )

        return Response(BookingSerializer(booking).data, status=201)
