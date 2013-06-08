import SeedShift as SS
import Shift as S
import Unicodde as U
while True:
    codename = raw_input("Cypher Codename:")
    current = getattr(globals(),codename)
    getattr(current,raw_input("Decode or encode").lower())()
