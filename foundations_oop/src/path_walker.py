from pathlib import Path


class PathWalker:
    def __init__(self, root: Path):
        self.root = Path(root).resolve()

    def list_files(self, pattern="*"):
        return sorted(self.root.glob(pattern))
