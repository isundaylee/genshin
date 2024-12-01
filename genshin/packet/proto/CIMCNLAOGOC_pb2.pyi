from genshin.packet.proto import ICIKKBECHFO_pb2 as _ICIKKBECHFO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CIMCNLAOGOC(_message.Message):
    __slots__ = ("DNKLCNCGMKB", "item_id", "IELOACIJMLI", "PONLPMHONBA", "MDEPHHNKPOC", "avatar_id", "IMIOGMDOKCB")
    DNKLCNCGMKB_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    IELOACIJMLI_FIELD_NUMBER: _ClassVar[int]
    PONLPMHONBA_FIELD_NUMBER: _ClassVar[int]
    MDEPHHNKPOC_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    DNKLCNCGMKB: _containers.RepeatedCompositeFieldContainer[_ICIKKBECHFO_pb2.ICIKKBECHFO]
    item_id: int
    IELOACIJMLI: int
    PONLPMHONBA: int
    MDEPHHNKPOC: bool
    avatar_id: int
    IMIOGMDOKCB: int
    def __init__(self, DNKLCNCGMKB: _Optional[_Iterable[_Union[_ICIKKBECHFO_pb2.ICIKKBECHFO, _Mapping]]] = ..., item_id: _Optional[int] = ..., IELOACIJMLI: _Optional[int] = ..., PONLPMHONBA: _Optional[int] = ..., MDEPHHNKPOC: bool = ..., avatar_id: _Optional[int] = ..., IMIOGMDOKCB: _Optional[int] = ...) -> None: ...
