from poReader.PoFileReader import *

infilePath = "../po/ultimate-member-zh_CN.po"

if __name__ == "__main__":
    reader = PoFileReader()
    reader.read(infilePath)
    result = reader.get_data()
    for block in result.get_blocks():
        block.print()