class PoBlockFilter():
    def __init__(self):
        self._segments = []
        self._segments_map = []

    def process(self, raw_msg):
        self._segments, self._segments_map = self._filte_html(raw_msg)
        self._segments, self._segments_map = self._filte_symbols(self._segments, self._segments_map)

    def get_segments(self):
        return self._segments

    def get_segments_map(self):
        return self._segments_map

    def _filte_html(self, raw_str):
        sum = 0
        addl = 0
        addr = 0
        for c in raw_str:
            if c == "<":
                sum += 1
            elif c == ">":
                sum -= 1
            if sum < 0:
                addl += -sum
                sum = 0
        addr = sum
        fited_str = "<" * addl + raw_str + ">" * addr
        sum = 0
        segs = []
        segs_map = []
        seg = ""
        seg_flag = 1
        for idx in range(len(fited_str)):
            c = fited_str[idx]
            if idx == 0 and c == "<":
                seg_flag = 0
            if c == "<":
                if len(seg) > 0:
                    segs.append(seg)
                    segs_map.append(seg_flag)
                    seg_flag = 0
                    seg = ""
                sum += 1
                seg += c
                if idx == len(fited_str) - 1:
                    if len(seg) > 0:
                        segs.append(seg)
                        segs_map.append(seg_flag)
            elif c == ">":
                sum -= 1
                seg += c
                if idx == len(fited_str) - 1:
                    if len(seg) > 0:
                        segs.append(seg)
                        segs_map.append(seg_flag)
            elif sum == 0 and idx != 0 and c != ">":
                if len(seg) > 0 and seg_flag == 0:
                    segs.append(seg)
                    segs_map.append(seg_flag)
                    seg_flag = 1
                    seg = ""
                seg += c
                if idx == len(fited_str) - 1:
                    if len(seg) > 0:
                        segs.append(seg)
                        segs_map.append(seg_flag)
            elif idx == len(fited_str) - 1:
                if len(seg) > 0:
                    segs.append(seg)
                    segs_map.append(seg_flag)
            else:
                seg += c
        if addl > 0:
            segs[0] = segs[0][addl:]
        if addr > 0:
            segs[-1] = segs[-1][:-addr]
        return segs, segs_map

    def _filte_symbols(self, segs, segs_map):
        return segs, segs_map