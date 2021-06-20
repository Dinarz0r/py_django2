from django.core.exceptions import PermissionDenied
import time
import os


class AntiDdosMiddleware:
    """
    middleware, которое будет вносить задержку
    в несколько секунд при обработке для каждого n-го запроса.
    """
    count_request = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            AntiDdosMiddleware.count_request += 1
            print(AntiDdosMiddleware.count_request)
            response = self.get_response(request)
            if AntiDdosMiddleware.count_request == 5:
                AntiDdosMiddleware.count_request = 0
                raise PermissionDenied
            else:
                return response
        except PermissionDenied:
            time.sleep(5)
