# RASPBERRY-PI-devo

# This is an example Makefile that compiles and links the small
# c++ program that impliments the Hello World!! protocol.

# It consists of a target (hello) and the dependency (hello.cpp)
# which is recognized as a c++ source file for which there is a
# built in build rule.

ARTIFACTS = _hello.cpp hello.s hello.o hello
EXTRAS    = hello.cpp.lst hello.s.lst hello.nm hello.map

$(EXTRAS):	hello hello.cpp hello.s
	pr -n hello.cpp > hello.cpp.lst
	pr -n hello.s > hello.s.lst
	nm hello > hello.nm
	pr -n hello.nm > hello.map

hello:  hello.o
	g++ hello.o -o hello

hello.o:        hello.s
	g++ -c hello.s

hello.s:        _hello.cpp
	g++ -S _hello.cpp -o hello.s

_hello.cpp:	hello.cpp
	g++ -E hello.cpp > _hello.cpp 

clean:
	rm -f $(ARTIFACTS) $(EXTRAS) 


