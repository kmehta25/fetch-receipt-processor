from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Receipt, Item
from .serializer import ReceiptSerializer, ItemSerializer
from .tasks import calculate_points


class ReceiptProcessView(APIView):
    def post(self, request):
        serializer = ReceiptSerializer(data = request.data)
        if serializer.is_valid():
            receipt = serializer.save()
            return Response(
                {
                    'id': str(receipt.id)
                },
                status = status.HTTP_200_OK
            )

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ReceiptPointsView(APIView):
    def get(self, request, pk):
        try:
            receipt = Receipt.objects.get(id = pk)
            points = calculate_points(receipt)
            return Response(
                {
                    'points': points
                },
                status = status.HTTP_200_OK
            )
        except Receipt.DoesNotExist:
            return Response(
                {
                    'detail': 'No receipt found with the provided id'
                },
                status = status.HTTP_404_NOT_FOUND
            )
        
