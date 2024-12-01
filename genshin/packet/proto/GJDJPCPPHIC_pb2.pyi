from genshin.packet.proto import LDCECHMBPFH_pb2 as _LDCECHMBPFH_pb2
from genshin.packet.proto import CJCEKNNABGI_pb2 as _CJCEKNNABGI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GJDJPCPPHIC(_message.Message):
    __slots__ = ("PEEBJAOIKFC", "HOLKPJJEEIM", "OAJOOBGHAGM", "MCPPEKNBHFK")
    PEEBJAOIKFC_FIELD_NUMBER: _ClassVar[int]
    HOLKPJJEEIM_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    MCPPEKNBHFK_FIELD_NUMBER: _ClassVar[int]
    PEEBJAOIKFC: _containers.RepeatedCompositeFieldContainer[_LDCECHMBPFH_pb2.LDCECHMBPFH]
    HOLKPJJEEIM: _CJCEKNNABGI_pb2.CJCEKNNABGI
    OAJOOBGHAGM: int
    MCPPEKNBHFK: int
    def __init__(self, PEEBJAOIKFC: _Optional[_Iterable[_Union[_LDCECHMBPFH_pb2.LDCECHMBPFH, _Mapping]]] = ..., HOLKPJJEEIM: _Optional[_Union[_CJCEKNNABGI_pb2.CJCEKNNABGI, _Mapping]] = ..., OAJOOBGHAGM: _Optional[int] = ..., MCPPEKNBHFK: _Optional[int] = ...) -> None: ...
