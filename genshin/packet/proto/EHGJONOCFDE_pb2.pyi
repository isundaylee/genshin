from genshin.packet.proto import PropValue_pb2 as _PropValue_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EHGJONOCFDE(_message.Message):
    __slots__ = ("DCJIMBILOGP", "type")
    DCJIMBILOGP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DCJIMBILOGP: _PropValue_pb2.PropValue
    type: int
    def __init__(self, DCJIMBILOGP: _Optional[_Union[_PropValue_pb2.PropValue, _Mapping]] = ..., type: _Optional[int] = ...) -> None: ...
