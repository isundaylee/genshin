from genshin.packet.proto import AvatarEquipAffixInfo_pb2 as _AvatarEquipAffixInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AKCEDPBKKLN(_message.Message):
    __slots__ = ("JGCFECCDGAJ", "MEJLFKPFPGK")
    JGCFECCDGAJ_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    JGCFECCDGAJ: _AvatarEquipAffixInfo_pb2.AvatarEquipAffixInfo
    MEJLFKPFPGK: int
    def __init__(self, JGCFECCDGAJ: _Optional[_Union[_AvatarEquipAffixInfo_pb2.AvatarEquipAffixInfo, _Mapping]] = ..., MEJLFKPFPGK: _Optional[int] = ...) -> None: ...
