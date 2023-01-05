from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserReservedInfoSerializer

class UserOrdersView(APIView):
    def get(self, request):
        user = request.user
        seats = user.screenseat_set \
            .filter(is_reserved=True) \
            .prefetch_related('order_set',
                              'schedule__movie',
                              'schedule__screen',
                              'schedule__screen__theater',
                              'schedule')

        if not seats:
            return Response({'message': '예매 내역이 없습니다.'})

        serializer = UserReservedInfoSerializer(seats, many=True)
        return Response(serializer.data)
