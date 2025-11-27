import sys
if len(sys.argv)!=3:
 print("usage : pyhton script.py <init_bal> <dep_bal>")
 init_bal=1000
 dep_bal=200
else :
 script_name=sys.argv[0]
 init_bal=int(sys.argv[1])
 dep_bal=int(sys.argv[2])
total=init_bal+dep_bal
print("initial bal is ",init_bal)
print("deposit bal is ",dep_bal)
print("total is ",total)
