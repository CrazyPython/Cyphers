import string,sys
def reverse(s):
    return s[::-1]
encode = {' ':' '}
for l,revl in zip(string.letters,reverse(string.letters)):
    encode[l]=revl
decode = {' ':' '}
for l,revl in zip(string.letters,reverse(string.letters)):
    decode[l]=revl
def encode():
    c = raw_input("Message:")
    try:
        sys.stdout.write(encode[i])
    except KeyError:
        sys.stdout.write(i)
def decode():
    c = raw_input("Message:")
    try:
        sys.stdout.write(decode[i])
    except KeyError:
        sys.stdout.write(i)
if __name__ == '__main':
    while True:
    what = raw_input("Decode or encode").lower()
    if what == "decode":
        current = Decode
    elif what == "encode":
        current = Encode
    else:
        print "What?"
        continue
    c = raw_input("What message would you like to decode/encode?")
    for i in c:
        try:
            sys.stdout.write(current[i])
        except KeyError:
            sys.stdout.write(i)
    sys.stdout.write('\n')
    sys.stdout.flush()
