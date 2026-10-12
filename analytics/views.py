from django.shortcuts import render


def creator_dashboard(request):
    return render(request, "analytics/dashboard.html", {})
