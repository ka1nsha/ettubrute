import asyncio,hashlib
from aiohttp import ClientSession
from tqdm import tqdm
import datetime,csv

class StartEngine():


    def __init__(self,**kwargs):
        self.header = kwargs.get('header')
        self.errorPage = kwargs.get('error_page')
        self.urls = list(kwargs.get('urls'))
        self.result = {}

    def Start(self):
        """
           You must be setting belove on instance variable

           :param header: You must setting Prepation instance headers in here
           :param errorPage: You must setting MD5 hash of Preparition instance
           :param urls: Generated URLS by Preparition instance
           """
        loop = asyncio.get_event_loop()

        for i in tqdm(range(len(self.urls))):
            loop.run_until_complete(self.Request(self.urls[i],i))


    async def Request(self,url,indexItem):
        """

        :param url:
        :type url: str
        :return None:
        """
        async with ClientSession() as session:
            async with session.get(url,headers=self.header) as response:
                rstatus = response.status

                if rstatus < 300:
                    rs = await response.read()
                    hashComp = self.hashComparision(rs)

                    if hashComp == True:
                        self.result[indexItem] = {"URL":url,'Status Code':404}
                    else:
                        self.result[indexItem] = {"URL": url, 'Status Code': rstatus}
                else:
                    self.result[indexItem] = {"URL": url, 'Status Code': rstatus}


    def hashComparision(self,content):
        """

        :param content:
        :type content: str
        :return bool:
        """
        md5 = hashlib.md5(content).hexdigest()

        if md5 == self.errorPage:
            return True
        else:
            return False

    def csvCreator(self):
        """
        Have not any argument for running.
        :return: csvFile
        """

        dt = datetime.datetime.now()
        filename = f"{dt.year}-{dt.month}-{dt.day}.csv"

        with open(filename,'w') as file:
            fields = ['URL','Status Code']
            writer = csv.DictWriter(file,fieldnames=fields)
            for k,v in self.result.items():

                writer.writerow(v)
