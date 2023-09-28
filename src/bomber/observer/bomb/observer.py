from common.Entity import Entity


class Observer:
    def __init__(self) -> None:
        self.subjects = set()

    def attach(self, subject):
        self.subjects.add(subject)
    
    def notify(self, bomb: Entity):
        for subject in self.subjects:
            subject.update(bomb)

observer = Observer()