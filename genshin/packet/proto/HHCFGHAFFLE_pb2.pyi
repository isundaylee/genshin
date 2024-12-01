from genshin.packet.proto import GDMLPOEDPJO_pb2 as _GDMLPOEDPJO_pb2
from genshin.packet.proto import KPFOBLALBLC_pb2 as _KPFOBLALBLC_pb2
from genshin.packet.proto import OOKJDBINGHA_pb2 as _OOKJDBINGHA_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HHCFGHAFFLE(_message.Message):
    __slots__ = ("music_brief_info", "DNBEFLJLAMB", "DAAKPCOABEP", "music_record")
    MUSIC_BRIEF_INFO_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    DAAKPCOABEP_FIELD_NUMBER: _ClassVar[int]
    MUSIC_RECORD_FIELD_NUMBER: _ClassVar[int]
    music_brief_info: _GDMLPOEDPJO_pb2.GDMLPOEDPJO
    DNBEFLJLAMB: int
    DAAKPCOABEP: _KPFOBLALBLC_pb2.KPFOBLALBLC
    music_record: _OOKJDBINGHA_pb2.OOKJDBINGHA
    def __init__(self, music_brief_info: _Optional[_Union[_GDMLPOEDPJO_pb2.GDMLPOEDPJO, _Mapping]] = ..., DNBEFLJLAMB: _Optional[int] = ..., DAAKPCOABEP: _Optional[_Union[_KPFOBLALBLC_pb2.KPFOBLALBLC, str]] = ..., music_record: _Optional[_Union[_OOKJDBINGHA_pb2.OOKJDBINGHA, _Mapping]] = ...) -> None: ...
