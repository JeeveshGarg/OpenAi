from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Summary
from .serializers import SummarySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .text_generation import generate_text

# Create your views here.

@api_view(['GET', 'POST'])
def summary_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Summary.objects.all()
        serializer = SummarySerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SummarySerializer(data=request.data)
        lis = generate_text(serializer.initial_data['text'])
        serializer.initial_data['summary'] = lis
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)