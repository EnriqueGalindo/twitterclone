from django.shortcuts import render
from .models import Notification


def notifications_view(request):
    logged_in = request.user
    notifications = Notification.objects.filter(target_user=logged_in)
    for notification in notifications:
        notification.viewed = True
        notification.save()
    return render(request,
                  'notifications.html',
                  {'notifications': notifications}
                  )
