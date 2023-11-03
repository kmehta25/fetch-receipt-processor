from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Receipt, Item
from .serializer import ReceiptSerializer, ItemSerializer
from .tasks import calculate_points

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ReceiptProcessView(APIView):
    @swagger_auto_schema(
        request_body=ReceiptSerializer,
        responses={200: openapi.Response("Success", openapi.Schema(type=openapi.TYPE_OBJECT)),
                   400: "Bad Request"},
        operation_summary="Process a receipt",
        operation_description="Process a receipt and add it to the database."
    )
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
    @swagger_auto_schema(
        manual_parameters=[openapi.Parameter('id', openapi.IN_PATH, description="Receipt ID", type=openapi.TYPE_INTEGER)],
        responses={200: openapi.Response("Success", openapi.Schema(type=openapi.TYPE_OBJECT)),
                   404: "Receipt Not Found"},
        operation_summary="Calculate points for a receipt",
        operation_description="Calculate the points earned by a customer from a particular receipt."
    )
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
        
