from django.core.exceptions import PermissionDenied


class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ['127.0.0.1', '192.168.112.251']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            raise PermissionDenied

        response = self.get_response(request)

        return response


class BlockIPMiddleware:
    """
    middleware, позволяющее запрещать запросы
    с заранее определенного списка ip адресов.
    """
    allowed_ips = ['127.0.0.1']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        if ip in BlockIPMiddleware.allowed_ips:
            print(ip)
            raise PermissionDenied

        response = self.get_response(request)
        return response
