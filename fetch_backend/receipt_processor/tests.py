import json
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Receipt, Item

class ReceiptPointsAPITest(APITestCase):
    def create_receipt(self, retailer, purchase_date, purchase_time, items, total):
        return Receipt.objects.create(
            retailer=retailer,
            purchaseDate=purchase_date,
            purchaseTime=purchase_time,
            items=items,
            total=total
        )

    def test_retailer_name(self):
        data = {
            "retailer": "NewRetailer",
            "purchaseDate": "2023-11-04",
            "purchaseTime": "12:00",
            "items": [
                {
                    "shortDescription": "New Product",
                    "price": "7.99"
                }
            ],
            "total": "7.99"
        }
        response = self.client.post(reverse('receipts:receipt_process'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        receipt_id = response.data['id']

        response = self.client.get(reverse('receipts:receipt_points', args=[receipt_id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['points'], 11)

    def test_round_dollar(self):
        data = {
            "retailer": "AnotherRetailer",
            "purchaseDate": "2023-11-04",
            "purchaseTime": "15:30",
            "items": [
                {
                    "shortDescription": "Another Product",
                    "price": "12.00"
                }
            ],
            "total": "12.00"
        }
        response = self.client.post(reverse('receipts:receipt_process'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        receipt_id = response.data['id']

        response = self.client.get(reverse('receipts:receipt_points', args=[receipt_id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['points'], 103)

    def test_multiple_of_0_25(self):
        data = {
            "retailer": "NewStore",
            "purchaseDate": "2023-11-04",
            "purchaseTime": "14:15",
            "items": [
                {
                    "shortDescription": "Sample Item",
                    "price": "2.50"
                }
            ],
            "total": "2.50"
        }
        response = self.client.post(reverse('receipts:receipt_process'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        receipt_id = response.data['id']

        response = self.client.get(reverse('receipts:receipt_points', args=[receipt_id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['points'], 43)

    def test_two_items(self):
        data = {
            "retailer": "GroceryShop",
            "purchaseDate": "2023-11-04",
            "purchaseTime": "13:45",
            "items": [
                {
                    "shortDescription": "Item A",
                    "price": "1.25"
                },
                {
                    "shortDescription": "Item B",
                    "price": "2.75"
                }
            ],
            "total": "4.00"
        }
        response = self.client.post(reverse('receipts:receipt_process'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        receipt_id = response.data['id']

        response = self.client.get(reverse('receipts:receipt_points', args=[receipt_id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['points'], 93)

    def test_desc_len_mul_of_3(self):
        data = {
            "retailer": "SampleShop",
            "purchaseDate": "2023-11-04",
            "purchaseTime": "14:00",
            "items": [
                {
                    "shortDescription": "Prod",
                    "price": "5.00"
                }
            ],
            "total": "5.00"
        }
        response = self.client.post(reverse('receipts:receipt_process'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        receipt_id = response.data['id']

        response = self.client.get(reverse('receipts:receipt_points', args=[receipt_id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['points'], 95)

    def test_odd_day(self):
        data = {
            "retailer": "NewGrocery",
            "purchaseDate": "2023-11-03",
            "purchaseTime": "13:30",
            "items": [
                {
                    "shortDescription": "Sample Item",
                    "price": "6.00"
                }
            ],
            "total": "6.00"
        }
        response = self.client.post(reverse('receipts:receipt_process'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        receipt_id = response.data['id']

        response = self.client.get(reverse('receipts:receipt_points', args=[receipt_id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['points'], 91)

    def test_purchase_time(self):
        data = {
            "retailer": "Store123",
            "purchaseDate": "2023-11-04",
            "purchaseTime": "15:30",
            "items": [
                {
                    "shortDescription": "Item X",
                    "price": "7.50"
                }
            ],
            "total": "7.50"
        }
        response = self.client.post(reverse('receipts:receipt_process'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        receipt_id = response.data['id']

        response = self.client.get(reverse('receipts:receipt_points', args=[receipt_id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['points'], 45)
