import enum


class Opcode(enum.IntEnum):
    PlayerLoginReq = 6606
    WorldPlayerRTTNotify = 24903
    PlayerStoreNotify = 424
    AvatarDataNotify = 23485

    SceneEntityDisappearNotify = -1
    SceneEntityAppearNotify = -1
    UnionCmdNotify = -1
