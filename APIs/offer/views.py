from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from offer.models import Offer
from offer.serializers import OfferSerializer
from django.http import Http404
from docxtpl import DocxTemplate
import os
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from docx import Document


class OfferList(APIView):

    """
    List all specific offers
    """

    def get(self, request, format=None):
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)


class OfferManage(APIView):

    def get_object(self, first_name):
        try:
            return Offer.objects.get(first_name=first_name)
        except Offer.DoesNotExist:
            return Http404

    def get(self, request, first_name, format=None):
        offer = self.get_object(first_name)
        serializer = OfferSerializer(offer)
        return Response(serializer.data)

    def put(self, request, first_name, format=None):
        offer = self.get_object(first_name)
        serializer = OfferSerializer(offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, first_name, format=None):
        offer = self.get_object(first_name)
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenerateOffer(APIView):
    def post(self, request, format=None):

        data = request.data
        # parse courses
        courses = ''
        coursesList = data['courseList']
        for i in range(len(coursesList)):
            if i == 0:
                courses += coursesList[i]['name']
            else:
                courses += coursesList[i]['name']

        offerInfo = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'birthday': data['birthday'],
            'passport': data['passport'],
            'phone': data['phone'],
            'email': data['email'],
            'address': data['address'],
            'start_date': data['courseList'][0]['intake'],
            'courses': courses,
            'campus': 'Melbourne'
        }

        serializer = OfferSerializer(data=offerInfo)
        if serializer.is_valid():
            # serializer.save()
            name = offerInfo['first_name']
            birthday = offerInfo['birthday'].replace("-","")
            tpl = DocxTemplate('temp.docx')
            tpl.render(offerInfo)
            filename = 'LOO-'+ name + '-' + birthday +'.docx'
            filepath = 'offers/' + filename
            tpl.save(filepath)

            filepath = os.path.realpath(filepath)
            word_file = open(filepath, 'rb')
            length = word_file.tell()
            print(filepath)
            response = HttpResponse(FileWrapper(word_file), status=status.HTTP_201_CREATED, content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = 'attachment; filename="%s"' % filename
            response['Content-Length'] = length
            # response = Response(serializer.data, status=status.HTTP_201_CREATED)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
