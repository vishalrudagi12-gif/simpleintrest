import sys
principle = float (sys.argv[1])
rate = float(sys.argv[2])
time  = float(sys.argv[3])
intrest = (principle * rate * time)/ 100
print("simple intres: ", intrest)