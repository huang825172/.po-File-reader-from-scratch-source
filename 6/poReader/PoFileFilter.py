from PoDataStructs import *


class PoFileFilter:
    def __init__(self):
        self._file = PoFileStruct()
        self._filter = PoBlockFilter()

    def process(self, poFile):
        if isinstance(poFile, PoFile):
            for block in poFile.get_blocks():
                new_block = PoTranslateBlock()
                new_block.extra = block.extra
                for idx in range(len(block.msgid)):
                    new_unit = PoTranslateUnit()
                    if idx < len(block.msgstr):
                        new_unit.result = block.msgstr[idx]
                    self._filter.process(block.msgid[idx])
                    new_unit.segments = self._filter.get_segments()
                    new_unit.segments_map = self._filter.get_segments_map()
                    new_block.append_unit(new_unit)
                self._file.add_block(new_block)
        else:
            raise TypeError("process: poFile must be instance of PoFile")

    def get_file_struct(self):
        return self._file
