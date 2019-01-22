import requests, random, string, hashlib
from os.path import isfile, exists


def random_url_generator(size):
    """

    :param size:  Setting up URL width
    :type size: int
    :return: list object
    """
    chars = string.ascii_letters + string.digits
    url = []

    for i in range(size):
        word = random.choice(chars)
        url.append(word)
    url = ''.join(url)

    return url

def fileopener(filename,sep):
    """

    :param filename: Filename on workspace
    :type filename: str
    :param sep: Multiline Seperator
    :type sep: str
    :return: None
    """
    with open(filename,'r') as f:
        getLines = f.read().splitlines()
        if sep is None:
            parseWithSeperator = ''.join(getLines)
        else:
            parseWithSeperator = ''.join(getLines).split(sep=sep)

        return parseWithSeperator




class RequestPreparation:
    """
    :param header: You can set specified headers for requests. If your didn't set header would use default header of Firefox.
    :type header: str
    :param error_page: You can set manually if known 404 page.
    :type error_page: str
    :param append_header: Used specified header with default header(Optional)
    :type append_header: dict
    :return: None
    """

    def __init__(self, **kwargs):


        # Report Arrays
        self.fails = []
        self.success = []


        # Getting URL
        self.baseurl = kwargs.get('url')
        if self.baseurl is None:
            raise ValueError('Please set URL. I\'m not god.')

        # Setting up header
        self.header = kwargs.get('header')
        if self.header is None:
            self.header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/71.0.3578.98 Safari/537.36',
                'Accept-Encoding': 'gzip,deflate,br',
                'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, '
                          'image / apng, * / *;q = 0.8',
            }

        # Setting up 404 Page for wrong redirect or dummy configurations

        self.error_page = kwargs.get('error_page')

        if self.error_page is None:
            size = random.randint(10, 25)
            url = random_url_generator(size=size)
            self.error_page = '{}/{}'.format(self.baseurl, url)

        self.error_page_hash = self.calculateMD5errorpage()


        # Used specified header with default header
        self.append_header = kwargs.get('append_header')

        try:
            if type(self.append_header) is dict:
                for k,v in self.append_header.items():
                    self.header[k] = v
            else:
                raise TypeError('Append header function only accept dict object.')
        except TypeError:
            pass
        finally:
            pass

    def dirlist(self, **kwargs):
        """

        :param dirlist: filename
        :type dirlist: str
        :raises ValueError if not set dirlist filename on def
        :raises FileNotFoundError if not found dirlist file on workspace
        :return List of contains directories:
        :rtype list:
        """
        filename = kwargs.get('filename')
        seperator = kwargs.get('sep')

        if filename is None:
            raise ValueError('You can set dirlist file for dir fuzzing.')
        elif isfile(filename) is not True or exists(filename) is not True:
            raise FileNotFoundError('Didn\'t find dirlist file.')
        else:
            if seperator is None:
                self.fl = fileopener(filename=filename,sep=None)
            else:
                self.fl = fileopener(filename=filename,sep=seperator)


    def calculateMD5errorpage(self):

        """
        This function used of calculate md5 of got 404 response code.
        :return: md5
        """

        browser = requests.get(self.error_page, headers=self.header)
        content = browser.content
        md5 = hashlib.md5(content).hexdigest()

        return md5


    def prepareURLEndswith(self, **kwargs):
        """

        :param end: Extension end of urls. Eg: php or php,asp
        :type end: str
        :return: set
        """
        end = kwargs.get('end')
        end = end.split(',')

        self.urls = set()
        for i in self.fl:
            for e in end:
                url = f"{self.baseurl}/{i}.{e}"
                self.urls.add(url)

        return self.urls






