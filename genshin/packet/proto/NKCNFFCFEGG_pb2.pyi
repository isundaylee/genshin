from genshin.packet.proto import PAJKNPDPNMO_pb2 as _PAJKNPDPNMO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NKCNFFCFEGG(_message.Message):
    __slots__ = ("HKNMHPPCOKO", "EKPDNKEFLHI", "LCGPFJGDMFE")
    HKNMHPPCOKO_FIELD_NUMBER: _ClassVar[int]
    EKPDNKEFLHI_FIELD_NUMBER: _ClassVar[int]
    LCGPFJGDMFE_FIELD_NUMBER: _ClassVar[int]
    HKNMHPPCOKO: _containers.RepeatedCompositeFieldContainer[_PAJKNPDPNMO_pb2.PAJKNPDPNMO]
    EKPDNKEFLHI: _PAJKNPDPNMO_pb2.PAJKNPDPNMO
    LCGPFJGDMFE: bool
    def __init__(self, HKNMHPPCOKO: _Optional[_Iterable[_Union[_PAJKNPDPNMO_pb2.PAJKNPDPNMO, _Mapping]]] = ..., EKPDNKEFLHI: _Optional[_Union[_PAJKNPDPNMO_pb2.PAJKNPDPNMO, _Mapping]] = ..., LCGPFJGDMFE: bool = ...) -> None: ...
