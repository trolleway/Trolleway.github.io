## Python


### Remove directory with files
```
        directory='tmp'
        if os.path.exists(directory):
            import shutil
            shutil.rmtree('/'+tmp)
```

### Create directory if not exists

```
        directory='tmp'
        if not os.path.exists(directory):
            os.makedirs(directory)
```

### File walking in python

```
import os

for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        if f.endswith(".x"):
            x(os.path.join(dirpath, f))
        elif f.endswith(".xc"):
            xc(os.path.join(dirpath,f))
```

### Connect to PostGIS

```
class Processor:

    conn_string = "host=192.168.250.1 user=trolleway dbname=osm_ch3 password="
     
   
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True #для vaccuum 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    
```
 
