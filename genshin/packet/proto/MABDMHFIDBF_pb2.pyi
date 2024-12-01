from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import HAIAENBCDME_pb2 as _HAIAENBCDME_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MABDMHFIDBF(_message.Message):
    __slots__ = ("GJEBAJAJPII", "DKOAGLJAAFA", "AOBBJBFJFDL", "KNGJHMLLCNP")
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    DKOAGLJAAFA_FIELD_NUMBER: _ClassVar[int]
    AOBBJBFJFDL_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    DKOAGLJAAFA: _containers.RepeatedCompositeFieldContainer[_HAIAENBCDME_pb2.HAIAENBCDME]
    AOBBJBFJFDL: int
    KNGJHMLLCNP: int
    def __init__(self, GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., DKOAGLJAAFA: _Optional[_Iterable[_Union[_HAIAENBCDME_pb2.HAIAENBCDME, _Mapping]]] = ..., AOBBJBFJFDL: _Optional[int] = ..., KNGJHMLLCNP: _Optional[int] = ...) -> None: ...
