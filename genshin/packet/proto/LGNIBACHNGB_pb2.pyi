from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LGNIBACHNGB(_message.Message):
    __slots__ = ("FENOJPLGMGE", "item_list", "EJNINFFFKJP")
    FENOJPLGMGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    FENOJPLGMGE: _containers.RepeatedScalarFieldContainer[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    EJNINFFFKJP: int
    def __init__(self, FENOJPLGMGE: _Optional[_Iterable[int]] = ..., item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...