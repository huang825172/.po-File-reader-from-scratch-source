class PoBlock:
    def __init__(self):
        self.msgid = []
        self.msgstr = []
        self.extra = []

    def print(self):
        print("Msgid:", self.msgid)
        print("Msgstr:", self.msgstr)
        print("Extra:", self.extra)


class PoFile:
    def __init__(self):
        self._blocks = []

    def add_block(self, block):
        if isinstance(block, PoBlock):
            self._blocks.append(block)
        else:
            raise RuntimeError("add_block: block must be instance of PoBlock.")

    def get_blocks(self):
        return self._blocks
