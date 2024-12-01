from genshin.packet.proto import AvatarInfo_pb2 as _AvatarInfo_pb2
from genshin.packet.proto import GAIOBFEADPD_pb2 as _GAIOBFEADPD_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PLCGIEAONLG(_message.Message):
    __slots__ = ("NOLBCHIACJI", "ugc_avatar_info", "GKNIKFALMCC")
    NOLBCHIACJI_FIELD_NUMBER: _ClassVar[int]
    UGC_AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    GKNIKFALMCC_FIELD_NUMBER: _ClassVar[int]
    NOLBCHIACJI: _AvatarInfo_pb2.AvatarInfo
    ugc_avatar_info: _GAIOBFEADPD_pb2.GAIOBFEADPD
    GKNIKFALMCC: int
    def __init__(self, NOLBCHIACJI: _Optional[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]] = ..., ugc_avatar_info: _Optional[_Union[_GAIOBFEADPD_pb2.GAIOBFEADPD, _Mapping]] = ..., GKNIKFALMCC: _Optional[int] = ...) -> None: ...
