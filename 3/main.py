infilePath = "../po/ultimate-member-zh_CN.po"
outfilePath = "../out/out_ultimate-member_zh_CN.mid"
with \
        open(infilePath, 'r', encoding="UTF-8") as in_f, \
        open(outfilePath, 'w', encoding='UTF-8') as out_f:
    file_lines = in_f.readlines()
    file_entries = []
    idx = 0
    while idx < len(file_lines):
        line = file_lines[idx]
        if line.find("msgid") == 0:
            msgid = []
            msgstr = []
            while line.find("msgstr") != 0:
                idx += 1
                if len(line.replace('\n', '')) > 0:
                    msgid.append(line.replace('\n', '').replace('msgid','').strip())
                line = file_lines[idx]
            line = file_lines[idx]
            if len(line.replace('\n', '')) > 0:
                msgstr.append(line.replace('\n', '').replace('msgstr','').strip())
            while idx < len(file_lines) - 1 and len(line.replace('\n', '')) > 0:
                idx += 1
                line = file_lines[idx]
                if len(line.replace('\n', '')) > 0:
                    msgstr.append(line.replace('\n', '').replace('msgstr','').strip())
            file_entries.append((msgid, msgstr))
        idx += 1
    for entry in file_entries:
        out_f.write(str(entry) + '\n')
