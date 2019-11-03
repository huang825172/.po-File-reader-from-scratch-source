from poReader.PoFileReader import *
from poReader.PoFileFilter import *

infilePath = "../po/ultimate-member-zh_CN.po"

if __name__ == "__main__":
    reader = PoFileReader()
    filte = PoFileFilter()
    reader.read(infilePath)
    filte.process(reader.get_data())

    result = filte.get_file_struct()
    for b in result.get_blocks():
        for u in b.get_units():
            print(u.segments)
            print(u.segments_map)
            print()