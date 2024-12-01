from genshin.packet.proto import BOMACPDEPID_pb2 as _BOMACPDEPID_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FGDNJPJJKOH(_message.Message):
    __slots__ = ("item_list", "IHFLGBGNAJE", "EJNINFFFKJP")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    IHFLGBGNAJE_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_BOMACPDEPID_pb2.BOMACPDEPID]
    IHFLGBGNAJE: _containers.RepeatedScalarFieldContainer[int]
    EJNINFFFKJP: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_BOMACPDEPID_pb2.BOMACPDEPID, _Mapping]]] = ..., IHFLGBGNAJE: _Optional[_Iterable[int]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
