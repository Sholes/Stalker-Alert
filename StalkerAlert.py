#python program
#!/usr/bin/env python


import re


emails = open("H:\\fbproject\\test1.txt","r") #opens the file to analyze

resultsList = []


for line in emails:
    if "InitialChatFriendsList" in line: #recgonizes the beginning of a email message and adds a linebreak
       # newMessage = re.findall(r'\w\w\w\s\w\w\w.*', line)
        #matches=re.findall(r'\"([0-9]-2)\"',line)
        #address = re.findall(r'"[\d.-]+"', line)
        array= re.findall("[+]?\d+[\.]?\d*", line)
        i=0
        #for i in array:
        print array[9]
        #print address
        
    
        
 
    
      



emails.close()


