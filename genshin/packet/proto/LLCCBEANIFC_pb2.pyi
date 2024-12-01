from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from genshin.packet.proto import OLHEKLKENDN_pb2 as _OLHEKLKENDN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LLCCBEANIFC(_message.Message):
    __slots__ = ("JAHPPELNEDF", "FGAEINCCKDK")
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    FGAEINCCKDK_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    FGAEINCCKDK: _OLHEKLKENDN_pb2.OLHEKLKENDN
    def __init__(self, JAHPPELNEDF: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., FGAEINCCKDK: _Optional[_Union[_OLHEKLKENDN_pb2.OLHEKLKENDN, _Mapping]] = ...) -> None: ...
