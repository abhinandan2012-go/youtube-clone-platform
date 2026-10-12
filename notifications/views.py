from django.shortcuts import render


def notifications_list(request):
    return render(request, "notifications/list.html", {})


def mark_notification_read(request, notification_id):
    return render(request, "notifications/read.html", {"notification_id": notification_id})
