from common.Entity import Entity
from common.concurrancyForEach import concurrancy_for_each


class Subject:
    def __init__(self) -> None:
        self.subjects = []

    def attach(self, subject):
        self.subjects.append(subject)

    def __process_subjects(self, bomb, subjects):
        for subject in subjects:
                subject.update(bomb)


    def notify(self, bomb: Entity):
        concurrancy_for_each(self.__process_subjects, self.subjects, bomb)

subject = Subject()