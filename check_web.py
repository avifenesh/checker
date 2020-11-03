import urllib.request


# check if the code received from the site = 200

def check_url(url):
    return urllib.request.urlopen(url).getcode() == 200


if __name__ == '__main__':
    check_url()
