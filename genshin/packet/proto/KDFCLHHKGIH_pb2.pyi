from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KDFCLHHKGIH(_message.Message):
    __slots__ = ("LEJABMHMPPM", "KDFEDKCGFPM", "JFGEKMGJNCA", "CCKJPDCHOBJ", "HHOGHBECPNP")
    LEJABMHMPPM_FIELD_NUMBER: _ClassVar[int]
    KDFEDKCGFPM_FIELD_NUMBER: _ClassVar[int]
    JFGEKMGJNCA_FIELD_NUMBER: _ClassVar[int]
    CCKJPDCHOBJ_FIELD_NUMBER: _ClassVar[int]
    HHOGHBECPNP_FIELD_NUMBER: _ClassVar[int]
    LEJABMHMPPM: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    KDFEDKCGFPM: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    JFGEKMGJNCA: bool
    CCKJPDCHOBJ: int
    HHOGHBECPNP: int
    def __init__(self, LEJABMHMPPM: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., KDFEDKCGFPM: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., JFGEKMGJNCA: bool = ..., CCKJPDCHOBJ: _Optional[int] = ..., HHOGHBECPNP: _Optional[int] = ...) -> None: ...
