import pythonping


def ping(ip, result=None, index=None, timeout=10, count=3, interval=1):
    try:
        response = pythonping.ping(ip, timeout=timeout, count=count, interval=interval)
    except Exception as e:
        print(ip, e)
        if result is None:
            return True, 254
        else:
            result[index] = True, 254
    if result is None:
        return response.success(), min(max(1, round(response.rtt_avg * 10)), 250)
    else:
        result[index] = response.success(), max(1, round(response.rtt_avg*10))


if __name__ == '__main__':
    print(ping('8.8.8.8'))
    print(ping('8.8.4.4'))
