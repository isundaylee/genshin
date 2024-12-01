from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LDFJJJDEFOA(_message.Message):
    __slots__ = ("GAIBIDBIBLK", "AHHFCLEFKNE", "LIJKCMJPIEC", "KFPHEMBCEFN", "DDNKDJJNNCI")
    GAIBIDBIBLK_FIELD_NUMBER: _ClassVar[int]
    AHHFCLEFKNE_FIELD_NUMBER: _ClassVar[int]
    LIJKCMJPIEC_FIELD_NUMBER: _ClassVar[int]
    KFPHEMBCEFN_FIELD_NUMBER: _ClassVar[int]
    DDNKDJJNNCI_FIELD_NUMBER: _ClassVar[int]
    GAIBIDBIBLK: _containers.RepeatedScalarFieldContainer[int]
    AHHFCLEFKNE: _containers.RepeatedScalarFieldContainer[int]
    LIJKCMJPIEC: _JICKPPDLOHC_pb2.JICKPPDLOHC
    KFPHEMBCEFN: int
    DDNKDJJNNCI: int
    def __init__(self, GAIBIDBIBLK: _Optional[_Iterable[int]] = ..., AHHFCLEFKNE: _Optional[_Iterable[int]] = ..., LIJKCMJPIEC: _Optional[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]] = ..., KFPHEMBCEFN: _Optional[int] = ..., DDNKDJJNNCI: _Optional[int] = ...) -> None: ...
