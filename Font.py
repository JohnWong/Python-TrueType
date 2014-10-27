# import mmap
import struct
import StringIO
import codecs

def readShort(stream):
    result = struct.unpack(">H", stream.read(2))
    return result[0]

def readInt(stream):
    result = struct.unpack(">i", stream.read(4))
    return result[0]

def readLong(stream):
    result = struct.unpack(">L", stream.read(4))
    return result[0]
 
def readChars(stream,count):
    s = stream.read(count)
    return s

def readTableEntry(reader):
    tag = readChars(reader, 4)
    check_sum = readLong(reader)
    offset = readLong(reader)
    length = readLong(reader)
    return (tag, check_sum, offset, length)

def readHead(f, offset):
    f.seek(offset)
    stream = f.stream
    major_ver = readShort(stream)
    minor_ver = readShort(stream)
    font_revison = readInt(stream)
    check_sum_adjustment = readInt(stream)
    magic_num = hex(readInt(stream))
    
    print(major_ver, minor_ver, font_revison, magic_num)

def readFile():
    datafile = r'/Users/john/Desktop/LLIconfont.ttf'
    with codecs.open(datafile, "r", "utf8", "ignore") as f:
        stream = f.stream
        major_ver = readShort(stream)
        minor_ver = readShort(stream)
        numbers_of_tables = readShort(stream)
        search_range = readShort(stream)
        entry_selector = readShort(stream)
        range_shift = readShort(stream)
        
        print("%d.%d" % (major_ver, minor_ver))
        print("numbers_of_tables", numbers_of_tables)
        print("search_range", search_range)
        print("entry_selector", entry_selector)
        print("range_shift", range_shift)

        for i in range(numbers_of_tables):
            table_entry = readTableEntry(stream)
            print("table_entry", table_entry)

        t = readHead(f, 268)    

readFile()