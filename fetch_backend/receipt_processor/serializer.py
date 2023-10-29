from rest_framework import serializers
from .models import Receipt, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['shortDescription', 'price']
    
class ReceiptSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many = True)

    class Meta:
        model = Receipt
        fields = [
            'id',
            'retailer',
            'purchaseDate',
            'purchaseTime',
            'total',
            'items'
        ]

    retailer = serializers.CharField(max_length = 225)
    purchaseDate = serializers.DateField()
    purchaseTime = serializers.TimeField()
    total = serializers.DecimalField(max_digits = 6, decimal_places = 2)

    def to_internal_value(self, data):
        # Strip leading and trailing whitespaces from relevant fields
        data['retailer'] = data.get('retailer', '').strip()
        items_data = data.get('items', [])
        for item_data in items_data:
            item_data['shortDescription'] = item_data.get('shortDescription', '').strip()
        return super().to_internal_value(data)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        receipt = Receipt.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(receipt = receipt, **item_data)
        
        return receipt
