
# Generator

simple python generator of static web photo gallery


```
docker build -f Dockerfile -t trolleway_website:dev .
cd ..
docker run --rm -it -v ${PWD}:/opt/website trolleway_website:dev  /bin/bash
```
In container run:
```

time python3 generator/run.py
```