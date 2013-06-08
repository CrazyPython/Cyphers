import string,sys
def reverse(s):
    return s[::-1]
encode = {' ':' '}
for l,revl in zip(string.letters,reverse(string.letters)):
    encode[l]=revl
decode = {' ':' '}
for l,revl in zip(string.letters,reverse(string.letters)):
    decode[l]=revl
while True:
    what = raw_input("Decode or encode").lower()
    if what == "decode":
        current = decode
    elif what == "encode":
        current = encode
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
