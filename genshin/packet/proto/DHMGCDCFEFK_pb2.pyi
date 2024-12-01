from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DHMGCDCFEFK(_message.Message):
    __slots__ = ("item_list", "GCFFNLEKKJH", "FAGPPHACNBJ", "EJNINFFFKJP")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    GCFFNLEKKJH_FIELD_NUMBER: _ClassVar[int]
    FAGPPHACNBJ_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    GCFFNLEKKJH: _containers.RepeatedScalarFieldContainer[int]
    FAGPPHACNBJ: int
    EJNINFFFKJP: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., GCFFNLEKKJH: _Optional[_Iterable[int]] = ..., FAGPPHACNBJ: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
