from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GNNCFJNLELC(_message.Message):
    __slots__ = ("item_list", "NKANJIJNIMC", "HIGAIJPFLAG", "HNNEELKCDMC", "PDCFPHKDHLH")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    NKANJIJNIMC_FIELD_NUMBER: _ClassVar[int]
    HIGAIJPFLAG_FIELD_NUMBER: _ClassVar[int]
    HNNEELKCDMC_FIELD_NUMBER: _ClassVar[int]
    PDCFPHKDHLH_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    NKANJIJNIMC: str
    HIGAIJPFLAG: int
    HNNEELKCDMC: int
    PDCFPHKDHLH: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., NKANJIJNIMC: _Optional[str] = ..., HIGAIJPFLAG: _Optional[int] = ..., HNNEELKCDMC: _Optional[int] = ..., PDCFPHKDHLH: _Optional[int] = ...) -> None: ...
