from genshin.packet.proto import PBHONEEKPMB_pb2 as _PBHONEEKPMB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EGBGHOPMDOB(_message.Message):
    __slots__ = ("KABODNMEGEK", "NEKECFNAHOM", "MPNJAOCKMAH")
    KABODNMEGEK_FIELD_NUMBER: _ClassVar[int]
    NEKECFNAHOM_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    KABODNMEGEK: _containers.RepeatedCompositeFieldContainer[_PBHONEEKPMB_pb2.PBHONEEKPMB]
    NEKECFNAHOM: int
    MPNJAOCKMAH: int
    def __init__(self, KABODNMEGEK: _Optional[_Iterable[_Union[_PBHONEEKPMB_pb2.PBHONEEKPMB, _Mapping]]] = ..., NEKECFNAHOM: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
