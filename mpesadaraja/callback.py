# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt  
# def process_stk_callback(request):
#     if request.method == 'POST':
#         try:
#             stk_callback_response = json.loads(request.body.decode('utf-8'))
            
#             merchant_request_id = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('MerchantRequestID')
#             checkout_request_id = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('CheckoutRequestID')
#             result_code = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('ResultCode', '')
#             result_desc = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('ResultDesc', '')
#             transaction_id = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('CallbackMetadata', {}).get('Item', [])[1].get('Value')
            
#             if not merchant_request_id or not checkout_request_id or not result_code:
#                 return JsonResponse({'message': 'Missing or invalid data in callback request'}, status=400)
            
#             amount = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('CallbackMetadata', {}).get('Item', [])[0].get('Value')
#             phone_number = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('CallbackMetadata', {}).get('Item', [])[4].get('Value')
            
#             if result_code == '0':
#                 donation = Donation(
#                     phone_number=phone_number,
#                     amount=amount,
#                     transaction_id=transaction_id
#                 )
#                 donation.save()
#                 print('Donation successful')
#                 return JsonResponse({'message': 'Donation confirmed and transaction completed'})
#             else:
#                 return JsonResponse({'message': f'Donation not confirmed: {result_desc}'}, status=400)
#         except json.JSONDecodeError as e:
#             return JsonResponse({'message': 'Invalid JSON data in callback request'}, status=400)
#     elif request.method == 'GET':
#         return JsonResponse({'message': 'This endpoint expects POST requests for processing M-Pesa STK callbacks.'})
#     else:
#         return JsonResponse({'message': 'Method not allowed'}, status=405)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process_stk_callback(request):
    if request.method == 'POST':
        try:
            stk_callback_response = json.loads(request.body.decode('utf-8'))

            merchant_request_id = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('MerchantRequestID')
            checkout_request_id = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('CheckoutRequestID')
            result_code = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('ResultCode', '')
            result_desc = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('ResultDesc', '')
            callback_metadata = stk_callback_response.get('Body', {}).get('stkCallback', {}).get('CallbackMetadata', {})

            if not merchant_request_id or not checkout_request_id or not result_code:
                return JsonResponse({'message': 'Missing or invalid data in callback request'}, status=400)

            amount_item = next((item for item in callback_metadata.get('Item', []) if item.get('Name') == 'Amount'), None)
            phone_item = next((item for item in callback_metadata.get('Item', []) if item.get('Name') == 'PhoneNumber'), None)
            transaction_id_item = next((item for item in callback_metadata.get('Item', []) if item.get('Name') == 'MpesaReceiptNumber'), None)

            amount = amount_item.get('Value') if amount_item else None
            phone_number = phone_item.get('Value') if phone_item else None
            transaction_id = transaction_id_item.get('Value') if transaction_id_item else None

            if result_code == '0' and amount and phone_number and transaction_id:
                print('STK push successful')
                return JsonResponse({'message': 'STK push confirmed and transaction completed'})
            else:
                return JsonResponse({'message': f'STK push not confirmed: {result_desc}'}, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Invalid JSON data in callback request'}, status=400)
    elif request.method == 'GET':
        return JsonResponse({'message': 'This endpoint expects POST requests for processing M-Pesa STK callbacks.'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
