from genshin.packet.proto import BargainSnapshot_pb2 as _BargainSnapshot_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BargainStartNotify(_message.Message):
    __slots__ = ("snapshot", "bargain_id")
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    BARGAIN_ID_FIELD_NUMBER: _ClassVar[int]
    snapshot: _BargainSnapshot_pb2.BargainSnapshot
    bargain_id: int
    def __init__(self, snapshot: _Optional[_Union[_BargainSnapshot_pb2.BargainSnapshot, _Mapping]] = ..., bargain_id: _Optional[int] = ...) -> None: ...
