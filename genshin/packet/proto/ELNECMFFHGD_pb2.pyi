from genshin.packet.proto import OPHOIIMINJJ_pb2 as _OPHOIIMINJJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ELNECMFFHGD(_message.Message):
    __slots__ = ("EGHEPPOLOJA", "IGBDOEBPPHO", "EJNINFFFKJP")
    EGHEPPOLOJA_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    EGHEPPOLOJA: _containers.RepeatedCompositeFieldContainer[_OPHOIIMINJJ_pb2.OPHOIIMINJJ]
    IGBDOEBPPHO: int
    EJNINFFFKJP: int
    def __init__(self, EGHEPPOLOJA: _Optional[_Iterable[_Union[_OPHOIIMINJJ_pb2.OPHOIIMINJJ, _Mapping]]] = ..., IGBDOEBPPHO: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
