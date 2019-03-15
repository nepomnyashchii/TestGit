with open('test1.txt', 'r') as f:
    print(f.read())
    print(f.mode)

with open('test1.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

with open('test1.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

with open('/Users/3/Desktop/test1.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)
    f_contents = f.readline()
    print(f_contents)

with open('test1.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')
    f_contents = f.readline()
    print(f_contents, end='')

with open('/Users/3/Desktop/test1.txt', 'r') as f:
    for line in f:
        print(line, end='')

with open('/Users/3/Desktop/test1.txt', 'r') as f:
    f_contents = f.read(34)
    print(f_contents)
with open('/Users/3/Desktop/test1.txt', 'r') as f:
    f_contents = f.read(7)
    print(f_contents)
    f_contents = f.read(7)
    print(f_contents)
with open('/Users/3/Desktop/test1.txt', 'r') as f:
    size_to_read = 12
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
with open('/Users/3/Desktop/test1.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
with open('/Users/3/Desktop/test1.txt', 'r') as f:
    size_to_read = 5
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
with open('/Users/3/Desktop/test2.txt', 'r') as f:
    size_to_read = 15
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
with open('/Users/3/Desktop/test1.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f.seek(0)
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

with open('/Users/3/Desktop/test1.txt', 'r') as rf:
    with open('/Users/3/Desktop/copy.test1.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
with open('/Users/3/Desktop/4.jpg', 'rb') as rf:
    with open('/Users/3/Desktop/copy.4.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

with open('/Users/3/Desktop/001.jpg', 'rb') as rf:
    with open('/Users/3/Desktop/copy.001.jpg', 'wb') as wf:
        chunk_size = 20
        rf_chunk = rf.read(chunk_size)
        while chunk_size > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
