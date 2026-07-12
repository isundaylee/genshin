import enum


class Opcode(enum.IntEnum):
    PlayerLoginReq = 5014
    WorldPlayerRTTNotify = 23697
    PlayerStoreNotify = 25494
    AvatarDataNotify = 22826

    SceneEntityDisappearNotify = -1
    SceneEntityAppearNotify = -1
    UnionCmdNotify = -1
