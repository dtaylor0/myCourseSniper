#!/usr/bin/env python
#updateIndex.py updates the file that holds the indices to search for in classScanner.py
import sys
def main():
    with open("indexSrc.txt",mode='r+') as f:
        print "Here are your current indices:"
        print "-----"
        print f.read().strip()
        print "-----"
        while True:
            print "Enter 0 (add index), 1 (remove index), or 2 (print indeces). Enter -1 to exit."
            operation=int(raw_input("Operation: "))
            if operation==0:
                print 'add'
                newIndex=raw_input('index: ')
                f.write(newIndex+'\n')
            elif operation==1:
                print 'remove'
                badIndex=raw_input('index: ')
                output=[]
                f.seek(0,0)
                for line in f:
                    if not line.strip()==badIndex:
                        output.append(line)
                        continue
                f.seek(0,0)
                f.truncate(0)
                f.writelines(output)
            elif operation==2:
                print 'print'
                f.seek(0,0)
                print '-----'
                print f.read().strip()
                print '-----'
            elif operation==-1:
                print 'exiting.'
                sys.exit()
            else:
                print "Bad input."
                continue

if __name__=='__main__':
    main()
