from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JHDENDCPNJL(_message.Message):
    __slots__ = ("KDFDIOOGGAL", "item_list", "FAGPPHACNBJ", "EJNINFFFKJP")
    KDFDIOOGGAL_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    FAGPPHACNBJ_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    KDFDIOOGGAL: _containers.RepeatedScalarFieldContainer[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    FAGPPHACNBJ: int
    EJNINFFFKJP: int
    def __init__(self, KDFDIOOGGAL: _Optional[_Iterable[int]] = ..., item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., FAGPPHACNBJ: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
