from genshin.packet.proto import MGDODHJHLCP_pb2 as _MGDODHJHLCP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JCJCMAIBCAO(_message.Message):
    __slots__ = ("PMEDIKCGDHM", "guid")
    PMEDIKCGDHM_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    PMEDIKCGDHM: _containers.RepeatedCompositeFieldContainer[_MGDODHJHLCP_pb2.MGDODHJHLCP]
    guid: int
    def __init__(self, PMEDIKCGDHM: _Optional[_Iterable[_Union[_MGDODHJHLCP_pb2.MGDODHJHLCP, _Mapping]]] = ..., guid: _Optional[int] = ...) -> None: ...
