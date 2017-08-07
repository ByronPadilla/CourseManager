class Student:
    def __init__(self, the_name: str, the_id: str):
        self._name = the_name
        self._id = the_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> str:
        return self._id

    def __hash__(self) -> int:
        return hash(self.id)

if __name__ == '__main__':
    pass