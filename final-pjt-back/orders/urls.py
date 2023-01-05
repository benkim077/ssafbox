from django.urls import path

from orders.views import KakaopayReadyAPI, KakaopaySuccessAPI, KakaopayCancelAPI, KakaopayFailAPI

app_name = 'orders'

urlpatterns = [
    path('kakaopay/ready/', KakaopayReadyAPI.as_view(), name='kakaopay-ready'),
    path('kakaopay/<str:uuid>/success/', KakaopaySuccessAPI.as_view(), name='kakaopay-success'),
    path('kakaopay/<str:uuid>/cancel/', KakaopayCancelAPI.as_view(), name='kakaopay-cancel'),
    path('kakaopay/<str:uuid>/fail/', KakaopayFailAPI.as_view(), name='kakaopay-fail'),
]
