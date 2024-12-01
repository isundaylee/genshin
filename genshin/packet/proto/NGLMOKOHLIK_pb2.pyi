from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NGLMOKOHLIK(_message.Message):
    __slots__ = ("BLGJDDIDBNF", "item_list", "FINAHGLFHAG", "EJNINFFFKJP")
    BLGJDDIDBNF_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    FINAHGLFHAG_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BLGJDDIDBNF: _containers.RepeatedScalarFieldContainer[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    FINAHGLFHAG: int
    EJNINFFFKJP: int
    def __init__(self, BLGJDDIDBNF: _Optional[_Iterable[int]] = ..., item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., FINAHGLFHAG: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
