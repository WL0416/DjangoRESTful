from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Offer
from .serializers import OfferSerializer

@csrf_exempt
def offer_list(request):
    """
    List all specific offers
    """
    if request.method == 'GET':
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OfferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def offer_manage(request, first_name):
    try:
        offer = Offer.objects.get(first_name=first_name)
        print(offer)
    except Offer.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = OfferSerializer(offer)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OfferSerializer(offer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        offer.delete()
        return HttpResponse(status=204)