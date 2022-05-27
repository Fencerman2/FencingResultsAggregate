import re


def trim_fredsid(url):
    trimmed_url = re.sub("&FREDSID=\w+", "", url)
    return trimmed_url
