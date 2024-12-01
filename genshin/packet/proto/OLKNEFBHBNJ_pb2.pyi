from genshin.packet.proto import IFPNJPJLNOF_pb2 as _IFPNJPJLNOF_pb2
from genshin.packet.proto import IALLEKKFHCL_pb2 as _IALLEKKFHCL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OLKNEFBHBNJ(_message.Message):
    __slots__ = ("LANJBJGNBOH", "IPCLFKLDKFA", "OAJOOBGHAGM")
    LANJBJGNBOH_FIELD_NUMBER: _ClassVar[int]
    IPCLFKLDKFA_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    LANJBJGNBOH: _containers.RepeatedCompositeFieldContainer[_IFPNJPJLNOF_pb2.IFPNJPJLNOF]
    IPCLFKLDKFA: _containers.RepeatedCompositeFieldContainer[_IALLEKKFHCL_pb2.IALLEKKFHCL]
    OAJOOBGHAGM: int
    def __init__(self, LANJBJGNBOH: _Optional[_Iterable[_Union[_IFPNJPJLNOF_pb2.IFPNJPJLNOF, _Mapping]]] = ..., IPCLFKLDKFA: _Optional[_Iterable[_Union[_IALLEKKFHCL_pb2.IALLEKKFHCL, _Mapping]]] = ..., OAJOOBGHAGM: _Optional[int] = ...) -> None: ...
