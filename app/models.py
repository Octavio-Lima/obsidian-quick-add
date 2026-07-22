class Vault:
    name: str
    path: str
    id: str
    is_default: bool

    def __init__(self, path: str, id: str, is_default: bool) -> None:
        self.name = path.split("/").pop().split("\\").pop()
        self.path = path
        self.id = id
        self.is_default = is_default
