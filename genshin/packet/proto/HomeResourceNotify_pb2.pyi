from genshin.packet.proto import HomeResource_pb2 as _HomeResource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeResourceNotify(_message.Message):
    __slots__ = ("home_coin", "fetter_exp")
    HOME_COIN_FIELD_NUMBER: _ClassVar[int]
    FETTER_EXP_FIELD_NUMBER: _ClassVar[int]
    home_coin: _HomeResource_pb2.HomeResource
    fetter_exp: _HomeResource_pb2.HomeResource
    def __init__(self, home_coin: _Optional[_Union[_HomeResource_pb2.HomeResource, _Mapping]] = ..., fetter_exp: _Optional[_Union[_HomeResource_pb2.HomeResource, _Mapping]] = ...) -> None: ...
