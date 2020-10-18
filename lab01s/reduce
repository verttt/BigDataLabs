from operator import itemgetter
import sys

current_country = None
current_totalpayout = 0.0
country = None

for line in sys.stdin:
   line = line.strip()
   country, payout = line.split('\t', 1)

   try:
     payout = float(payout)
   except ValueError:
     continue

   if current_country == country:
        current_totalpayout += payout
   else:
      if current_country:
         print(current_country + "\t" + str(current_totalpayout))
      current_country     = country
      current_totalpayout = payout

if current_country == country:
   print(current_country + "\t" + str(current_totalpayout))