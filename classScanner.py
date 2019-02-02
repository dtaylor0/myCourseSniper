#!/usr/bin/env python
#classScanner.py - scans Rutgers schedule of classes for openings of designated indexes

import sys,requests,json,os,time
from time import sleep
def main():
    indexArray=[]
    with open("indexSrc.txt",mode='r') as f:
        for line in f:
            indexArray.append(line.strip())
    #url="http://sis.rutgers.edu/soc/api/openSections.gzip?year=2019&term=1&campus=NB"
    url="http://sis.rutgers.edu/soc/api/openSections.gzip"
    info={('year',str(2019)),('term',str(1)),('campus','NB')}
    while True:
        print 'Timestamp: '+(time.strftime('%m/%d/%Y %I:%M:%S'))+'  Checking indices...\n-----'
        for index in indexArray:
            print index
        print '-----'
        subjects = requests.get(url,params=info)
        subjects.raise_for_status()
        subjects=subjects.json()
        openClasses=[]
        for index in indexArray:
            for item in subjects:
                if item==index:
                    openClasses.append(index)
                    break

        for index in openClasses:
            print index+' is open!'
        registerCommand='./webregBot.py'
        for index in openClasses:
            registerCommand+=' '+index
        if len(openClasses)>0:
            os.system(registerCommand)
            for index in openClasses:
                for i in indexArray:
                    if index==i:
                        indexArray.remove(i)
        print 'Sleeping...\nPress ctrl-c to stop.\n'
        sleep(60)

if __name__=='__main__':
    main()
