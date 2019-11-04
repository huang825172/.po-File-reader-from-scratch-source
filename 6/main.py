from poReader.PoFileReader import PoFileReader
from poReader.PoFileFilter import PoFileFilter
from poTranslators import BaiduTranslator

infilePath = "../po/ultimate-member-zh_CN.po"
infilePath = "../po/wedevs-project-manager-zh_CN.po"

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
            # if len(u.segments)>0 and len(u.segments[0])>0:
            #     print(BaiduTranslator.translate_auto(u.segments[0]))
            # print()
