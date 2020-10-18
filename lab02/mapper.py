#!/opt/anaconda/envs/bd9/bin/python

import happybase
import sys


def main():
   def  map(line):
      def h_emit(key, ts, url):
          table.put(key, {'data:url' : url}, timestamp = int(ts))
          for k, d in table.scan():
             print(k, d)
		  
      objects = line.split('\t')
      if len(objects) == 3:
         uid, timestamp, url = objects
         try:
             i_uid = int(uid)
             timestamp_ex = int(float(timestamp) * 1000)	
         except Exception:
             i_uid = 0 
         if i_uid % 256 == 154 and url.startswith('http'):
             h_emit(uid, timestamp_ex, url)
   connection = happybase.Connection('bd-node2.newprolab.com')
   connection.open()
   families = {
       'data':  dict(max_versions = 10),
       'cf2':   dict(max_versions = 1, block_cache_enabled = False),
       'cf3':   dict(),
              }
   #try: 		  
   #   connection.create_table('alexander.vertyagin', families) 
   #except Exception:
   #   connection.disable_table('alexander.vertyagin')
   #   connection.delete_table('alexander.vertyagin', disable = False) 
   #   connection.create_table('alexander.vertyagin', families) 	  
   
   table = connection.table(b'alexander.vertyagin')

   #print(connection.tables())

   for line in sys.stdin:
       map(line.strip())
   connection.close()

if  __name__ == '__main__':
    main()
