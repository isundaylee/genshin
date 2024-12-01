from genshin.packet.proto import PlayerRTTInfo_pb2 as _PlayerRTTInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldPlayerRTTNotify(_message.Message):
    __slots__ = ("CBNMCBCHMNA",)
    CBNMCBCHMNA_FIELD_NUMBER: _ClassVar[int]
    CBNMCBCHMNA: _containers.RepeatedCompositeFieldContainer[_PlayerRTTInfo_pb2.PlayerRTTInfo]
    def __init__(self, CBNMCBCHMNA: _Optional[_Iterable[_Union[_PlayerRTTInfo_pb2.PlayerRTTInfo, _Mapping]]] = ...) -> None: ...
