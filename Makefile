$(CC)=gcc
$(CFLAGS)=-c -g

all: foo

foo: foo.o
	$(CC) -o foo foo.o

foo.o: foo.c
	$(CC) $(CFLAGS) foo.c

.PHONY: clean

clean:
	rm *.o foo
