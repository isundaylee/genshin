from genshin.packet.proto import HomeResource_pb2 as _HomeResource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeResourceTakeFetterExpRsp(_message.Message):
    __slots__ = ("retcode", "fetter_exp")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    FETTER_EXP_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    fetter_exp: _HomeResource_pb2.HomeResource
    def __init__(self, retcode: _Optional[int] = ..., fetter_exp: _Optional[_Union[_HomeResource_pb2.HomeResource, _Mapping]] = ...) -> None: ...
