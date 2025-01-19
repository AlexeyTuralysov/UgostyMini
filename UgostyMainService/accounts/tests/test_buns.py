from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from accounts.models import Buns
""" models.py
class Buns(models.Model):
    name = models.CharField(max_length=120)
    img_buns = models.ImageField(upload_to='buns')
    price = models.IntegerField(default=0)
    created_at = models.CharField(max_length=50)
    color_treats = models.TextField(max_length=120)
    
"""


class BunsApiTestCase(APITestCase):
    def setUp(self):
        Buns.objects.create(name="pirogock", img_buns="/media/buns/pirogock.png", price=64, created_at="2024-09-20", color_treats="#EDSA21")


    def testGetBuns(self):
        url = reverse('buns-list')
        """urls.py
        path('api/buns/', BunsListView.as_view(), name='buns-list'),
        """

        getBuns = self.client.get(url)

        self.assertEqual(getBuns.status_code, status.HTTP_200_OK)

        bun = getBuns.data[0]
        self.assertEqual(bun['name'], "pirogock")
        self.assertEqual(bun['price'], 64)

        print("Название плюшки", bun['name'],'\n'
              "Цена", bun['price'], '\n'
              "Цвет на плашки на статистике", bun['color_treats'])


