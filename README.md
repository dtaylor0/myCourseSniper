# myCourseSniper

for Rutgers University

### What:
This is a Python script using requests to access the Rutgers SOC(Schedule of Classes) API to find open courses and then using selenium to open the page(webreg) where I register for classes and to fill in the open sections for me, so that I just have to press submit.


### Why:
I made this personal course sniper because the similar services that are available to me and that are used by many students at Rutgers only check about every 15 minutes to see if a course has opened (although I believe one of them has a paid membership that checks the SOC API more frequently).  I can use this to check at any time interval I want, and in its current form it checks every minute.

### Overview:
**indexSrc.txt** - file meant to hold all class section indices that I am currently sniping in this format:
```
00001
00002
00003
...
```

**credentials.py** - contains a dictionary holding a 'username' and a 'password' to sign into webreg once openings are found.

#####Example file contents:
```
login={'username':'your_username','password':'your_password'}
```
**classScanner.py** - periodically gets the list of open indices from the SOC API, compares the indices in indexSrc.txt to the ones just recieved, and calls webregBot.py if any matches are found.  Also shows timestamp of each API access and prints all indices it checks from indexSrc.txt

**webregBot.py** - takes in arguments of up to 10 indices (10 is the limit of webreg's registration page), opens Firefox, creates appropriate URL with all indices included and navigates to the URL, uses credentials from credentials.py to login to webreg, and awaits the user to submit the indices for registration if they choose to.

**updateIndex.py** - allows the user to add, delete, or print indices in the indexSrc.txt file.


### Possible improvements:
- Create a way to update the semester info used in the URL instead of hard coding it; this can probably be done in a very similar way to how the indices were stored and updated.
- Put names to indices, a.k.a. use SOC API to show classes associated with each index being sniped.
