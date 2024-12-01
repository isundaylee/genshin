from genshin.packet.proto import AODEBPFBIML_pb2 as _AODEBPFBIML_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AAKBIJIKBNM(_message.Message):
    __slots__ = ("IALAGDBIKKD", "DHHFPPCCNED", "EAIPGEMKNPO")
    IALAGDBIKKD_FIELD_NUMBER: _ClassVar[int]
    DHHFPPCCNED_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    IALAGDBIKKD: _containers.RepeatedCompositeFieldContainer[_AODEBPFBIML_pb2.AODEBPFBIML]
    DHHFPPCCNED: _containers.RepeatedScalarFieldContainer[int]
    EAIPGEMKNPO: int
    def __init__(self, IALAGDBIKKD: _Optional[_Iterable[_Union[_AODEBPFBIML_pb2.AODEBPFBIML, _Mapping]]] = ..., DHHFPPCCNED: _Optional[_Iterable[int]] = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
