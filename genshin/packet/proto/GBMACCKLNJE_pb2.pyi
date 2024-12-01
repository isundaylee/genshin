from genshin.packet.proto import OLHEKLKENDN_pb2 as _OLHEKLKENDN_pb2
from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GBMACCKLNJE(_message.Message):
    __slots__ = ("FGAEINCCKDK", "JAHPPELNEDF")
    FGAEINCCKDK_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    FGAEINCCKDK: _OLHEKLKENDN_pb2.OLHEKLKENDN
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    def __init__(self, FGAEINCCKDK: _Optional[_Union[_OLHEKLKENDN_pb2.OLHEKLKENDN, _Mapping]] = ..., JAHPPELNEDF: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ...) -> None: ...
