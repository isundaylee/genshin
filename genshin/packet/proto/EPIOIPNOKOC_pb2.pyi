from genshin.packet.proto import BPOBBMNGMDL_pb2 as _BPOBBMNGMDL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EPIOIPNOKOC(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _BPOBBMNGMDL_pb2.BPOBBMNGMDL
    def __init__(self, type: _Optional[_Union[_BPOBBMNGMDL_pb2.BPOBBMNGMDL, str]] = ...) -> None: ...
