import sys

for line in sys.stdin:
   line = line.strip()
   ip, userid, country, bannerid, payout = line.strip().split(",")
   print(country + "\t" + str(payout))
