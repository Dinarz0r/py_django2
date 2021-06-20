def check_access_by_age(age):
    if age < 18:
        return False
    return True


def open_clock(time: int) -> bool:
    time_open = [i for i in range(8, 13)] + [i for i in range(14, 20 + 1)]
    if time in time_open:
        return True
    return False


def text_connection(str1, str2):
    return str1 + str2
