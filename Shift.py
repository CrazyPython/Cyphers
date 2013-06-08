#ALL LOWERCASE! no spaces/punctuation
import random,string
def tonum(s):
    return string.ascii_lowercase.index(s)
def tochr(n):
    while n > 26:
        n-=26
    return string.ascii_lowercase[n]
def encode():
    s = raw_input("Shift:")
    message = raw_input("Message:")
    numbers = [tonum(i) for i in message]
    message = ''.join([tochr(n+s) for n,s in zip(numbers,shift)])
    print "Message:"+message+" Seed:"+seed
def encode():
    s = raw_input("Shift:")
    message = raw_input("Message:")
    numbers = [tonum(i) for i in message]
    message = ''.join([tochr(n+s) for n,s in zip(numbers,shift)])
    print "Message:"+message+" Seed:"+seed
