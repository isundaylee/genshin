from genshin.packet.proto import LIBNNJIADME_pb2 as _LIBNNJIADME_pb2
from genshin.packet.proto import ACJBAFCALIN_pb2 as _ACJBAFCALIN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GBGADBFFGOO(_message.Message):
    __slots__ = ("quest_param", "level", "chapter_id", "NBKBEFDEOBP", "MLIOFJEOKLG")
    QUEST_PARAM_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHAPTER_ID_FIELD_NUMBER: _ClassVar[int]
    NBKBEFDEOBP_FIELD_NUMBER: _ClassVar[int]
    MLIOFJEOKLG_FIELD_NUMBER: _ClassVar[int]
    quest_param: _LIBNNJIADME_pb2.LIBNNJIADME
    level: int
    chapter_id: int
    NBKBEFDEOBP: _ACJBAFCALIN_pb2.ACJBAFCALIN
    MLIOFJEOKLG: int
    def __init__(self, quest_param: _Optional[_Union[_LIBNNJIADME_pb2.LIBNNJIADME, _Mapping]] = ..., level: _Optional[int] = ..., chapter_id: _Optional[int] = ..., NBKBEFDEOBP: _Optional[_Union[_ACJBAFCALIN_pb2.ACJBAFCALIN, str]] = ..., MLIOFJEOKLG: _Optional[int] = ...) -> None: ...
