import os
import datetime


class LoggedInfo:
    """
    middleware, позволяющее запрещать запросы
    с заранее определенного списка ip адресов.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.log_path = os.path.abspath(os.path.join('advertisements', 'logging', 'save_log.log'))

    def __call__(self, request):
        ip_client = request.META.get('REMOTE_ADDR')

        request_method = request.META.get('REQUEST_METHOD')
        HTTP_USER_AGENT = request.META.get('HTTP_USER_AGENT')
        req_url = request.get_full_path()
        if not os.path.isfile(self.log_path):
            make_dirs_path = os.path.abspath(os.path.join(self.log_path, '../'))
            os.makedirs(make_dirs_path)
        with open(self.log_path, 'a', encoding='utf-8') as log:
            log.write(f'\n{datetime.datetime.now()}\n'
                      f'IP клиента: {ip_client}\n'
                      f'Запрошенный URL: {req_url}\n'
                      f'Метод обращения: {request_method}\n'
                      f'User-agent: {HTTP_USER_AGENT}\n')



        response = self.get_response(request)

        return response
