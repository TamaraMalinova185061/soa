import enum


class DogStatus(enum.IntEnum):
    LOST = 0
    WAITING = 1
    SHELTERED = 2
    RESERVED = 3
    RESCUED = 4


class LostDogReportStatus(enum.IntEnum):
    OPENED = 0
    CLOSED = 1

class DogBreed(enum.Enum):
    MALTESE = "maltese"
    CORGI = "corgi"
    POODLE = "poodle"
    PUG = "pug"
    BICHON = "bichon"
    POMERANIAN = "pomeranian"
    BOXER = "boxer"
