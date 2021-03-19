from rest_framework.decorators import api_view
from rest_framework.response import Response

from analytics.models import User, Stream


@api_view(['POST'])
def user_create(request):
    user_id = request.data['user_id']

    if len(User.objects.filter(user_id=user_id)) > 0:
        return Response(status=400)
    else:
        user = User(user_id=user_id)
        user.save()

        return Response(status=200)


@api_view(['POST'])
def stream_finish(request):
    stream_id = request.data['stream_id']
    user_id = request.data['user_id']

    stream_duration = request.data['stream_duration']
    user_count = request.data['user_count']
    sales_count = request.data['sales_count']

    if len(Stream.objects.filter(stream_id=stream_id)) == 0:
        users = User.objects.filter(user_id=user_id)
        if len(users) == 1:
            conversion = sales_count / user_count

            stream = Stream(stream_id=stream_id, user=users[0],
                            stream_duration=stream_duration, user_count=user_count, sales_count=sales_count,
                            conversion=conversion)
            stream.save()

            return Response(status=200)
        else:
            return Response(status=400)
    else:
        return Response(status=400)
