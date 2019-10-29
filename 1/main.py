infilePath = "../po/ultimate-member-zh_CN.po"
outfilePath = "../out/out_ultimate-member_zh_CN.po"
with \
        open(infilePath, 'r', encoding="UTF-8") as inf, \
        open(outfilePath, 'w', encoding='UTF-8') as outf:
    for line in inf.readlines():
        outf.write(line)
