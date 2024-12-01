from genshin.packet.proto import ENFMOPIEEMA_pb2 as _ENFMOPIEEMA_pb2
from genshin.packet.proto import JBJFCEKCLGE_pb2 as _JBJFCEKCLGE_pb2
from genshin.packet.proto import JAEPBKGEDDL_pb2 as _JAEPBKGEDDL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GEEMAADBNJI(_message.Message):
    __slots__ = ("GODOGIJJJIA", "GLKNGDDNOCN", "music_info", "balloon_info", "fall_info", "IEJPGHNLIDB")
    GODOGIJJJIA_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    MUSIC_INFO_FIELD_NUMBER: _ClassVar[int]
    BALLOON_INFO_FIELD_NUMBER: _ClassVar[int]
    FALL_INFO_FIELD_NUMBER: _ClassVar[int]
    IEJPGHNLIDB_FIELD_NUMBER: _ClassVar[int]
    GODOGIJJJIA: int
    GLKNGDDNOCN: bool
    music_info: _ENFMOPIEEMA_pb2.ENFMOPIEEMA
    balloon_info: _JBJFCEKCLGE_pb2.JBJFCEKCLGE
    fall_info: _JAEPBKGEDDL_pb2.JAEPBKGEDDL
    IEJPGHNLIDB: int
    def __init__(self, GODOGIJJJIA: _Optional[int] = ..., GLKNGDDNOCN: bool = ..., music_info: _Optional[_Union[_ENFMOPIEEMA_pb2.ENFMOPIEEMA, _Mapping]] = ..., balloon_info: _Optional[_Union[_JBJFCEKCLGE_pb2.JBJFCEKCLGE, _Mapping]] = ..., fall_info: _Optional[_Union[_JAEPBKGEDDL_pb2.JAEPBKGEDDL, _Mapping]] = ..., IEJPGHNLIDB: _Optional[int] = ...) -> None: ...
