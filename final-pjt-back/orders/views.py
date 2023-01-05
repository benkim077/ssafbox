import json
import uuid
import datetime

import requests
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Order
from screens.models import ScreenSeat
from ssafbox.settings import KAKAO_ADMIN_KEY
from ssafbox.utils import SEAT_OCCUPY_TIME_LIMIT


class KakaopayReadyAPI(APIView):
    def post(self, request, *args, **kwargs):
        url = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": f"KakaoAK {KAKAO_ADMIN_KEY}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        seats_no = request.data.get('seats_no')

        seats = ScreenSeat.objects.get(pk=seats_no)
        duration = datetime.datetime.now(datetime.timezone.utc) - seats.last_updated
        print(seats.last_updated)
        if duration.total_seconds() > 300:
            return Response("예매시간 초과", status=400)

        order_id = str(uuid.uuid4())
        user_id = 1
        total_price = 10000

        order = Order.objects.create(
            user_id=user_id,
            uuid=order_id,
            total_price=total_price,
            seats=seats,
        )

        params = {
            'cid': "TC0ONETIME",
            'partner_order_id': order_id,
            'partner_user_id': user_id,
            'item_name': '영화관 티켓',
            'quantity': 1,
            'total_amount': 10000,
            'tax_free_amount': 0,
            'approval_url': f"http://localhost:8080/ticket/payment/{order_id}/success",
            'cancel_url': f"http://localhost:8080/ticket/payment/{order_id}/cancel",
            'fail_url': f"http://localhost:8080/ticket/payment/{order_id}/fail",
        }

        response = requests.post(url, headers=headers, data=params)
        response = json.loads(response.text)

        order.tid = response.get('tid')
        order.save()
        return Response(response)


class KakaopaySuccessAPI(APIView):
    def get(self, request, *args, **kwargs):
        _uuid = self.kwargs.get('uuid')
        pg_token = request.GET.get('pg_token')
        order = Order.objects.get(uuid=_uuid)
        tid = order.tid
        url = 'https://kapi.kakao.com/v1/payment/approve'
        headers = {
            "Authorization": f"KakaoAK {KAKAO_ADMIN_KEY}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        params = {
            'cid': "TC0ONETIME",
            'tid': tid,
            'partner_order_id': _uuid,
            'partner_user_id': order.user_id,
            'pg_token': pg_token,
        }
        response = requests.post(url, headers=headers, data=params)
        response = json.loads(response.text)
        order.is_paid = True
        order.save()
        seat = order.seats
        seat.is_reserved = True
        seat.save()
        return Response(response)


class KakaopayCancelAPI(APIView):
    def get(self, request, *args, **kwargs):
        pass


class KakaopayFailAPI(APIView):
    def get(self, request, *args, **kwargs):
        pass
