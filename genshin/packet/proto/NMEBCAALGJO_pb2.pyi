from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NMEBCAALGJO(_message.Message):
    __slots__ = ("item_list", "GPKNHHNJCFI", "DNBEFLJLAMB", "PIPCKJELPIJ")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    GPKNHHNJCFI_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    PIPCKJELPIJ_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    GPKNHHNJCFI: int
    DNBEFLJLAMB: int
    PIPCKJELPIJ: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., GPKNHHNJCFI: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ..., PIPCKJELPIJ: _Optional[int] = ...) -> None: ...
