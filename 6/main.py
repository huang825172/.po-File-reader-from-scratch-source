from poIO.PoFileReader import PoFileReader
from poIO.PoFileFilter import PoFileFilter
from poIO.PoUnitConnector import PoUnitConnector
from Translators import BaiduTranslator

infilePath = "../po/ultimate-member-zh_CN.po"
infilePath = "../po/wedevs-project-manager-zh_CN.po"
outfilePath = "../out/out_wedevs-project-manager-zh_CN.out"

if __name__ == "__main__":
    reader = PoFileReader()
    filte = PoFileFilter()
    reader.read(infilePath)
    filte.process(reader.get_data())
    outf = open(outfilePath, 'w', encoding='utf-8')

    result = filte.get_file_struct()
    connect = PoUnitConnector()
    for b in result.get_blocks():
        for u in b.get_units():
            connect.set_unit(u)
            translate_list = connect.get_translate_list()
            translated_list = []
            for line in translate_list:
                res = BaiduTranslator.translate_auto(line)
                translated_list.append(('' if res is None else res))
            res_list = connect.set_translate_list(translated_list)
            outf.write(str(res_list) + '\n')
            print(res_list)
            # if len(u.segments)>0 and len(u.segments[0])>0:
            #     print(BaiduTranslator.translate_auto(u.segments[0]))
            # print()

    outf.close()
