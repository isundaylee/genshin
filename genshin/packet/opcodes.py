import enum


class Opcode(enum.IntEnum):
    PlayerLoginReq = 6606
    WorldPlayerRTTNotify = 24903

    SceneEntityDisappearNotify = -1
    SceneEntityAppearNotify = -1
    UnionCmdNotify = -1
