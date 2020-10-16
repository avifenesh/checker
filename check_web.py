import urllib.request


def check_url(url):
    return urllib.request.urlopen(url).getcode() == 200


if __name__ == '__main__':
    check_url()
