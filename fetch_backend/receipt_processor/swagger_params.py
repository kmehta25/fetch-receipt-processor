from rest_framework import serializers
from drf_yasg import openapi

item_param = openapi.Parameter(
    name="items",
    in_=openapi.IN_BODY,
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(
        type=openapi.TYPE_OBJECT,
        properties={
            "shortDescription": openapi.Schema(type=openapi.TYPE_STRING),
            "price": openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    description="Items",
    required=True,
)

retailer_param = openapi.Parameter(
    name="retailer",
    in_=openapi.IN_BODY,
    type=openapi.TYPE_STRING,
    description="Retailer",
    required=True,
)

purchase_date_param = openapi.Parameter(
    name="purchaseDate",
    in_=openapi.IN_BODY,
    type=openapi.TYPE_STRING,
    format=openapi.FORMAT_DATE,
    description="Purchase Date",
    required=True,
)

purchase_time_param = openapi.Parameter(
    name="purchaseTime",
    in_=openapi.IN_BODY,
    type=openapi.TYPE_STRING,
    format=openapi.FORMAT_TIME,
    description="Purchase Time",
    required=True,
)

total_param = openapi.Parameter(
    name="total",
    in_=openapi.IN_BODY,
    type=openapi.TYPE_STRING,
    description="Total",
)

receipt_process_params = [retailer_param, purchase_date_param, purchase_time_param, item_param, total_param]

receipt_points_params = [
    openapi.Parameter(
        name="id",
        in_=openapi.IN_PATH,
        type=openapi.TYPE_INTEGER,
        description="Receipt ID",
        required=True,
    )
]