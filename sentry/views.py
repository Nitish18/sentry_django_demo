from django.http import HttpResponse
from sentry_sdk import capture_message


def home(request):
    capture_message("Page not found 2222!", level="error")
    return HttpResponse('Hello, World!')
