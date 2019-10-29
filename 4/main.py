import re

infilePath = "../po/ultimate-member-zh_CN.po"
outfilePath = "../out/out_ultimate-member_zh_CN.mid"


def strip_rn(line_str):
    return line_str.replace('\n', '').replace('\r', '').strip()


def strip_line(line_str):
    pattern = re.compile('(?<=\")(.+?)(?=\")')
    result = pattern.search(line_str)
    if result is None:
        return ""
    else:
        return result.group().strip()


try:
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
                    if len(strip_rn(line)) > 0:
                        msgid.append(strip_line(line))
                    line = file_lines[idx]
                line = file_lines[idx]
                if len(strip_rn(line)) > 0:
                    msgstr.append(strip_line(line))
                while idx < len(file_lines) - 1 and len(strip_rn(line)) > 0:
                    idx += 1
                    line = file_lines[idx]
                    if len(strip_rn(line)) > 0:
                        msgstr.append(strip_line(line))
                file_entries.append((msgid, msgstr))
            idx += 1
        for entry in file_entries:
            out_f.write(str(entry) + '\n')
except Exception as e:
    print(e)
