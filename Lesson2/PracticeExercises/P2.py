# Convert the names to a "Last, First" format

beatles = ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"]

for name in beatles:
    spaceIndex = name.index(" ");
    first = name[:spaceIndex];
    last = name[spaceIndex+1:];
    print last + ", " + first;

