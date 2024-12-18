print("Hello World")
print("Kiran Bhan Singh")
#print(*objects, sep=' ', end='\n', file=None, flush=False)
#Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.

#All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.

#The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead.

#Output buffering is usually determined by file. However, if flush is true, the stream is forcibly flushed.

#Changed in version 3.3: Added the flush keyword argument.

print("Kiran",123,"Bhan",345,"Singh")
print("Kiran",123,"Bhan",345,"Singh", sep="-")
print("Kiran",123,"Bhan",345,"Singh", sep="**")
