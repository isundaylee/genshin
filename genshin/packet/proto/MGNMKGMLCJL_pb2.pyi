from genshin.packet.proto import HCJGIFNJPPJ_pb2 as _HCJGIFNJPPJ_pb2
from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MGNMKGMLCJL(_message.Message):
    __slots__ = ("IBEAKHHNOHB", "MFIGIDKAJBD", "CILMGHAMEDD", "DDLKLKOGOOD")
    IBEAKHHNOHB_FIELD_NUMBER: _ClassVar[int]
    MFIGIDKAJBD_FIELD_NUMBER: _ClassVar[int]
    CILMGHAMEDD_FIELD_NUMBER: _ClassVar[int]
    DDLKLKOGOOD_FIELD_NUMBER: _ClassVar[int]
    IBEAKHHNOHB: _HCJGIFNJPPJ_pb2.HCJGIFNJPPJ
    MFIGIDKAJBD: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    CILMGHAMEDD: int
    DDLKLKOGOOD: bool
    def __init__(self, IBEAKHHNOHB: _Optional[_Union[_HCJGIFNJPPJ_pb2.HCJGIFNJPPJ, _Mapping]] = ..., MFIGIDKAJBD: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., CILMGHAMEDD: _Optional[int] = ..., DDLKLKOGOOD: bool = ...) -> None: ...
