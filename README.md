# EttuBrute

I know this tool wasn't to do Brute-Force tool but i loved that name.

This tool is faster than similar because it sends asynchronous requests. You can also see the % status on the CLI. This way you can guess where you are staying.At the end of the study you can see all the request and response codes on a csv file.


# Usage
You can see type to --help
```
usage: main.py [-h] [-url URL] [-d D] [-e E] [-sep SEP]

optional arguments:
  -h, --help  show this help message and exit
  -url URL    To set which domain to fuzzing. eg:https://enesergun.net
  -d D        File of Fuzzing extensions eg:dirlist.txt
  -e E        Set extension eg: php or php,asp
  -sep SEP    Seperator to extensions eg: ,
```

Example
```
python main.py -url http://www.enesergun.net/ -d dirlist.txt -e php -sep :
```

# Requirements

```
pip install -r requirements.txt
```

$> cat requirements.txt
```
aiohttp==3.5.4
async-timeout==3.0.1
asyncio==3.4.3
attrs==18.2.0
certifi==2018.11.29
chardet==3.0.4
idna==2.8
multidict==4.5.2
requests==2.21.0
tqdm==4.29.1
urllib3==1.24.1
yarl==1.3.0
aiohttp==3.5.4
async-timeout==3.0.1
asyncio==3.4.3
attrs==18.2.0
certifi==2018.11.29
chardet==3.0.4
idna==2.8
multidict==4.5.2
requests==2.21.0
tqdm==4.29.1
urllib3==1.24.1
yarl==1.3.0
aiohttp==3.5.4
async-timeout==3.0.1
asyncio==3.4.3
attrs==18.2.0
certifi==2018.11.29
chardet==3.0.4
idna==2.8
multidict==4.5.2
requests==2.21.0
tqdm==4.29.1
urllib3==1.24.1
yarl==1.3.0
```

