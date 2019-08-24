#C++ Makefile
CC=g++

VERSION=-std=c++14
CFLAGS=-c -fPIC
LDFLAGS=
PNAME=hello


all: build

build: map.o
	$(CC) $(VERSION) -shared -Wl,-soname,libmap.so -o libmap.so map.o

map.o: map.cpp
	$(CC) $(CFLAGS) $(VERSION) map.cpp

clean:
	rm *o
	echo 'clean done...'
