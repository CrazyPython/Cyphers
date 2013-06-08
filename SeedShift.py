#ALL LOWERCASE! no spaces/punctuation
import random,string
def tonum(s):
    return string.ascii_lowercase.index(s)
def tochr(n):
    while n > 26:
        n-=26
    return string.ascii_lowercase[n]
def encode():
    seed = raw_input("Seed:")
    random.seed(seed)
    message = raw_input("Message:")
    shift = [random.randint(1,26) for i in range(len(message))]
    numbers = [tonum(i) for i in message]
    message = ''.join([tochr(n+s) for n,s in zip(numbers,shift)])
    print "Message:"+message+" Seed:"+seed
def decode():
    seed = raw_input("Seed:")
    random.seed(seed)
    message = raw_input("Message:")
    shift = [random.randint(1,26) for i in range(len(message))]
    numbers = [tonum(i) for i in message]
    message = ''.join([tochr(n-s) for n,s in zip(numbers,shift)])
    print "Message:"+message
