from genshin.packet.proto import HOPFEEIPGJP_pb2 as _HOPFEEIPGJP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BCDNFNMFIJC(_message.Message):
    __slots__ = ("AKGOOIIBCOM", "DMAGPFEPMPG", "OHEMOADEAJP", "HHDNNMNHNCI", "JKJHKFDNEPM", "NOFDMPEGGCE", "OILCNLIKKIB")
    AKGOOIIBCOM_FIELD_NUMBER: _ClassVar[int]
    DMAGPFEPMPG_FIELD_NUMBER: _ClassVar[int]
    OHEMOADEAJP_FIELD_NUMBER: _ClassVar[int]
    HHDNNMNHNCI_FIELD_NUMBER: _ClassVar[int]
    JKJHKFDNEPM_FIELD_NUMBER: _ClassVar[int]
    NOFDMPEGGCE_FIELD_NUMBER: _ClassVar[int]
    OILCNLIKKIB_FIELD_NUMBER: _ClassVar[int]
    AKGOOIIBCOM: _HOPFEEIPGJP_pb2.HOPFEEIPGJP
    DMAGPFEPMPG: _containers.RepeatedScalarFieldContainer[int]
    OHEMOADEAJP: int
    HHDNNMNHNCI: bool
    JKJHKFDNEPM: bool
    NOFDMPEGGCE: bool
    OILCNLIKKIB: int
    def __init__(self, AKGOOIIBCOM: _Optional[_Union[_HOPFEEIPGJP_pb2.HOPFEEIPGJP, _Mapping]] = ..., DMAGPFEPMPG: _Optional[_Iterable[int]] = ..., OHEMOADEAJP: _Optional[int] = ..., HHDNNMNHNCI: bool = ..., JKJHKFDNEPM: bool = ..., NOFDMPEGGCE: bool = ..., OILCNLIKKIB: _Optional[int] = ...) -> None: ...
