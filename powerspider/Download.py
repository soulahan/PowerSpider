import cchardetfrom requests import request, RequestExceptionfrom loguru import loggerdef downloader(url, method=None, header=None, timeout=None, binary=False, **kwargs):    logger.info(f'Scraping {url}')    _headers = {        'User-Agent': ('Mozilla/5.0 (compatible; MSIE 9.0; '                       'Windows NT 6.1; Win64; x64; Trident/5.0)'),    }    _maxTimeout = timeout if timeout else 5    _headers = header if header else _headers    _method = "GET" if not method else method    try:        response = request(method=_method, url=url, headers=header, **kwargs)        encoding = cchardet.detect(response.content)['encoding']        logger.info(f"Redirect_URL: {response.url}") if url != response.url else None        if response.status_code == 200:            return response.content if binary else response.content.decode(encoding)        logger.error('Get invalid status code %s while scraping %s', response.status_code, url)    except RequestException:        logger.error('error occurred while scraping %s', url, exc_info=True)if __name__ == '__main__':    print(downloader("https://www.baidu.com/", "GET"))# print(scrape_page('https://www.baidu.com'))# pass