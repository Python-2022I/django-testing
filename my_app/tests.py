from django.test import TestCase
from .models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")


    def test_animal_fields(self):
        '''Animal model fields'''
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")

        self.assertEqual(lion.sound, 'roar')
        self.assertEqual(cat.sound, 'meow')


    def test_animal_speak(self):
        '''Animal model speak method'''
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")

        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')



class AnimalViewTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animal_view_get(self):
        '''Animal view get method'''
        response = self.client.get('/api/animals/')

        output = [
            {
                "id": 1,
                "name": "lion",
                "sound": "roar"
            },
            {
                "id": 2,
                "name": "cat",
                "sound": "meow"
            }
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), output)

    def test_animail_view_get_pk(self):
        '''Animal view get method with pk'''
        response = self.client.get('/api/animals/1')

        output = {
            "id": 1,
            "name": "lion",
            "sound": "roar"
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), output)

    def test_animail_view_get_pk_not_found(self):
        '''Animal view get method with pk not found'''
        response = self.client.get('/api/animals/3')

        output = {
            "status": "errors"
        }

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), output)

    def test_animail_view_post(self):
        '''Animal view post method'''
        data = {
            "name": "dog",
            "sound": "bark"
        }
        response = self.client.post('/api/animals/', json=data)

        output = {
            "id": 3,
            "name": "dog",
            "sound": "bark"
        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), output)

