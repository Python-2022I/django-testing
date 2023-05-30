from django.http import HttpResponse, JsonResponse
from django.views import View
import json

from .models import Animal


class AnimalView(View):
    def get(self, request, pk: int = None):
        if pk is None:
            animals = Animal.objects.all()
            animals_json = [
                {
                    "id": animal.id, 
                    "name": animal.name, 
                    "sound": animal.sound
                } for animal in animals
            ]
            return JsonResponse(animals_json, safe=False, status=200)
        else:
            try:
                animal = Animal.objects.get(id=pk)
                return JsonResponse(
                    {
                        "id": animal.id, 
                        "name": animal.name, 
                        "sound": animal.sound
                    }, 
                    status=200
                )
            except Animal.DoesNotExist:
                return JsonResponse({"status": "errors"}, status=404)
    
    def post(self, request):
        data_json = request.body.decode("utf-8")
        data = json.loads(data_json)

        animal = Animal.objects.create(
            name=data["name"], 
            sound=data["sound"]
        )

        return JsonResponse(
            {
                "id": animal.id, 
                "name": animal.name, 
                "sound": animal.sound
            }, 
            status=201
        )
