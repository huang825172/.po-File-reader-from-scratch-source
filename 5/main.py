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


def read_block(lines):
    try:
        idx = 0
        block_entries = []
        while idx < len(lines):
            line = lines[idx]
            if line.find("msgid") == 0:
                msgid = []
                msgstr = []
                while line.find("msgstr") != 0:
                    idx += 1
                    if len(strip_rn(line)) > 0:
                        msgid.append(strip_line(line))
                    line = lines[idx]
                line = lines[idx]
                if len(strip_rn(line)) > 0:
                    msgstr.append(strip_line(line))
                while idx < len(lines) - 1 and len(strip_rn(line)) > 0:
                    idx += 1
                    line = lines[idx]
                    if len(strip_rn(line)) > 0:
                        msgstr.append(strip_line(line))
                block_entries.append((msgid, msgstr))
            idx += 1
        if len(block_entries) > 1:
            raise RuntimeError("Block have more than one entry.")
        return block_entries
    except Exception as e:
        print(e)


try:
    with \
            open(infilePath, 'r', encoding="UTF-8") as in_f, \
            open(outfilePath, 'w', encoding='UTF-8') as out_f:
        file_lines = in_f.readlines()
        file_blocks = []
        idx = 0
        start = 0
        for idx in range(len(file_lines)):
            line = file_lines[idx]
            if len(strip_rn(line)) == 0:
                file_blocks.append(file_lines[start:idx])
                start = idx + 1
            elif idx == len(file_lines) - 1:
                file_blocks.append(file_lines[start:])
        file_data = []
        for block in file_blocks:
            data = read_block(block)
            file_data.append(data)
            out_f.write(str(block) + '\n')
            out_f.write(str(data) + '\n')
            out_f.write('\n')
except Exception as e:
    print(e)
