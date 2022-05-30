from pathlib import Path

class Character:
    def __init__(self):
        self.name = 'unknown'
        self.voice = str(Path(Path.cwd(), 'resources', 'voices', 'Default.wav'))