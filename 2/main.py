infilePath = "../po/ultimate-member-zh_CN.po"
outfilePath = "../out/out_ultimate-member_zh_CN.po"
with \
        open(infilePath, 'r', encoding="UTF-8") as in_f, \
        open(outfilePath, 'w', encoding='UTF-8') as out_f:
    file_lines = in_f.readlines()
    idx = 0
    while idx < len(file_lines):
        line = file_lines[idx]
        if line.find("msgid") == 0:
            while line.find("msgstr") != 0:
                idx += 1
                out_f.write(line)
                line = file_lines[idx]
            line = file_lines[idx]
            out_f.write(line)
            while idx < len(file_lines) - 1 and len(line.replace('\n', '')) > 0:
                idx += 1
                line = file_lines[idx]
                out_f.write(line)
        idx += 1
