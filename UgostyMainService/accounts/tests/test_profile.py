from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class ProfileTestCase(APITestCase):
    def setUp(self):
        nameUrl = reverse('user_register')
        """ urls.py
         path('api/user/register/', RegisterView.as_view(), name='user_register'),
        """

        bodyRaw = {'username': 'Testregapi',
                   'email': 'test123456@gmail.com',
                   'password': 'password123456'
                   }


        sendPost = self.client.post(nameUrl, bodyRaw, format='json')

        self.assertEqual(sendPost.status_code, status.HTTP_201_CREATED)
        print(sendPost.data)


    def testProfile(self):
        url = reverse('user_profile', kwargs={'username': 'Testregapi'})
        sendGet = self.client.get(url, format='json')

        self.assertEqual(sendGet.status_code, status.HTTP_200_OK)
        print("ответ", sendGet.data)





