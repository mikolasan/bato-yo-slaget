# Makefile for embedded Python use demo.
# (This version originally written on Red Hat Linux 6.1;
# edit lines marked with XXX.)

# XXX The compiler you are using
CC=	 	gcc

# XXX Top of the build tree and source tree
blddir=		.
srcdir=		.

# Python version
VERSION=	2.7

# Compiler flags
OPT=		-fno-strict-aliasing -D_FORTIFY_SOURCE=2 -g -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security  -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes
INCLUDES=	-I/usr/include/python2.7 -I/usr/include/x86_64-linux-gnu/python2.7
CFLAGS=		$(OPT)
CPPFLAGS=	$(INCLUDES)

# The Python library

LIBPYTHON=	-L/usr/lib/python2.7/config-x86_64-linux-gnu -L/usr/lib

# XXX edit LIBS (in particular) to match $(blddir)/Makefile
LIBS=		-lpython2.7
LDFLAGS=	-Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions
SYSLIBS=	-lpthread -ldl  -lutil -lm
ALLLIBS=	$(LIBPYTHON) $(SYSLIBS) $(LIBS)

# Build the main applications
all:		main
main:		main.o
		$(CC) $(LDFLAGS) main.o $(ALLLIBS) -o main

# Administrative targets

test:		main
		./main

clean:
		-rm -f *.o core

clobber:	clean
		-rm -f *~ @* '#'* main

realclean:	clobber
