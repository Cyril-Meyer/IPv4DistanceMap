import pythonping


def ping(ip, result=None, index=None):
    try:
        response = pythonping.ping(ip, timeout=25, count=4, interval=1)
    except Exception as e:
        print(ip, e)
    if result is None:
        return response.success(), max(1, round(response.rtt_avg * 10))
    else:
        result[index] = response.success(), max(1, round(response.rtt_avg*10))


if __name__ == '__main__':
    print(ping('8.8.8.8'))
    print(ping('8.8.4.4'))
