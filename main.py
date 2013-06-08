import SeedShift as SS
import Unicodde as U
while True:
    current = getattr(globals(),raw_input("Cypher Codename:"))
    getattr(current,raw_input("Decode or encode").lower())()
