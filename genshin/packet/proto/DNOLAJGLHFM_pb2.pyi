from genshin.packet.proto import AvatarInfo_pb2 as _AvatarInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DNOLAJGLHFM(_message.Message):
    __slots__ = ("PIFPIOEEHKJ", "ACJFJMLFJEA")
    PIFPIOEEHKJ_FIELD_NUMBER: _ClassVar[int]
    ACJFJMLFJEA_FIELD_NUMBER: _ClassVar[int]
    PIFPIOEEHKJ: _AvatarInfo_pb2.AvatarInfo
    ACJFJMLFJEA: bool
    def __init__(self, PIFPIOEEHKJ: _Optional[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]] = ..., ACJFJMLFJEA: bool = ...) -> None: ...
