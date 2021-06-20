from django.core.exceptions import PermissionDenied
import time


class BlockDdosIPMiddleware:
    """
    middleware, которое будет возвращать ошибку
    если за последние 5 секунд было больше k запросов c одного ip адреса.
    """

    allowed_ips = []

    def __init__(self, get_response):
        self.get_response = get_response
        self.check_ip_dict = {}

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        ip_list = self.check_ip_dict
        if ip_list.get(ip) is None:
            ip_list[ip] = [time.time(), 1]
        elif time.time() - ip_list[ip][0] > 10:
            ip_list[ip] = None
        elif ip_list[ip][1] < 5 and time.time() - ip_list[ip][0] < 5:
            x = time.time() - ip_list[ip][0]
            ip_list[ip][1] += 1
            print(x)
        elif ip_list[ip][1] > 4 and time.time() - ip_list[ip][0] < 10:
            raise PermissionDenied
        response = self.get_response(request)
        return response
