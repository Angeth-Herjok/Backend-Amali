from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .stkPush import initiate_stk_push
from .generateAccesstoken import get_access_token
from .query import query_stk_status
from .callback import process_stk_callback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DarajaApiView(APIView):
    def post(self, request):
        body = request.data
        phone = body.get('phone_number')
        full_name = body.get('full_name')
        email = body.get('email')
        amount = body.get('amount', 0)
        
        success = initiate_stk_push(amount, phone, full_name, email)

        if success:
            response_data = {'message': 'Donation made successfully'}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {'message': 'Donation failed'}
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
