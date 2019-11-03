from . import PoDataStructs
from . import PoBlockFilters


class PoFileFilter:
    def __init__(self):
        self._file = PoDataStructs.PoFileStruct()
        self._filter = PoBlockFilters.PoBlockFilter()

    def process(self, poFile):
        if isinstance(poFile, PoDataStructs.PoFile):
            for block in poFile.get_blocks():
                new_block = PoDataStructs.PoTranslateBlock()
                new_block.extra = block.extra
                for idx in range(len(block.msgid)):
                    new_unit = PoDataStructs.PoTranslateUnit()
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
