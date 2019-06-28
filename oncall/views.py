from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pytz
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from oncall.models import Oncall
from oncall.serializers import OncallSerializer
# Create your views here.

def calendar_view(request):
    context = dict()
    return render(
        request,
        'oncall/schedule.html',
        context
    )
@csrf_exempt
def add_view(request):
    context = dict()
    return render(
        request,
        'oncall/add.html',
        context
    )

class OncallApi(APIView):

    def get(self, request):
        offset = self.request.query_params.get('timezone', None)
        if (offset) == None:
            offset = 0
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)
        if (start) and (end):
            if 'T' in start:
                tformat = "%Y-%m-%dT%H:%M:%S"
            else:
                tformat = "%Y-%m-%d"
            start = datetime.datetime.strptime(start, tformat).replace(tzinfo=pytz.utc)
            end = datetime.datetime.strptime(end, tformat).replace(tzinfo=pytz.utc)
            schedules = Oncall.objects.filter(start__range=[start, end])
        else:
            schedules = Oncall.objects.all()
        serialized = OncallSerializer(schedules, many=True, context={
            'offset': offset,
        })
        return Response(serialized.data)
    @csrf_exempt
    def post(self,request):
        serializer = OncallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)