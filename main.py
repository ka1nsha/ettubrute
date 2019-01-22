import preparation, engine

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-url",help='To set which domain to fuzzing. eg:https://enesergun.net')
parser.add_argument("-d",help="File of Fuzzing extensions eg:dirlist.txt")
parser.add_argument('-e',help="Set extension eg: php or php,asp")
parser.add_argument('-sep',help="Seperator to extensions eg: ,")

args = parser.parse_args()


prep = preparation.RequestPreparation(url=args.url)
prep.dirlist(filename=args.d,sep=args.sep)
urllist = prep.prepareURLEndswith(end=args.e)

engine = engine.StartEngine(header=prep.header,error_page=prep.error_page_hash,urls=urllist)
engine.Start()
engine.csvCreator()









