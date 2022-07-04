
# Generator

simple python generator of static web photo gallery


```
docker build -f Dockerfile -t trolleway_website:dev .
cd ..
docker run --rm -it -v ${PWD}:/opt/website -v c:\trolleway\website-storage\storage\:/opt/storage trolleway_website:dev  /bin/bash
```
In container run:
```

time python3 generator/run.py
```