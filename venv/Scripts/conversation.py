from anytree import Node
import json
from anytree.importer import DictImporter
from anytree import RenderTree
from pathlib import Path
import logging

class Conversation:
    def __init__(self, name):
        path = Path(Path.cwd(), 'resources', 'conversations')
        f = open(str(path / f'{name}.json'))
        data = json.load(f)
        importer = DictImporter()
        logging.debug(data)
        self.root = importer.import_(data)

    def print_conversation(self):
        print(RenderTree(self.root))

    def have_conversation(self, alpha, beta):
        print(RenderTree(self.root))


class Audio_Conversation(Conversation):
    def __init__(self, name):
        super().__init__(name)
