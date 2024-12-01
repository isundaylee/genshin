from genshin.packet.proto import KCJMDCFPOBF_pb2 as _KCJMDCFPOBF_pb2
from genshin.packet.proto import BLGLPAIGIFD_pb2 as _BLGLPAIGIFD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PCPPNCIBCIN(_message.Message):
    __slots__ = ("AHKLJDPLAEK", "MBLJACOLEIF")
    AHKLJDPLAEK_FIELD_NUMBER: _ClassVar[int]
    MBLJACOLEIF_FIELD_NUMBER: _ClassVar[int]
    AHKLJDPLAEK: _containers.RepeatedCompositeFieldContainer[_KCJMDCFPOBF_pb2.KCJMDCFPOBF]
    MBLJACOLEIF: _containers.RepeatedCompositeFieldContainer[_BLGLPAIGIFD_pb2.BLGLPAIGIFD]
    def __init__(self, AHKLJDPLAEK: _Optional[_Iterable[_Union[_KCJMDCFPOBF_pb2.KCJMDCFPOBF, _Mapping]]] = ..., MBLJACOLEIF: _Optional[_Iterable[_Union[_BLGLPAIGIFD_pb2.BLGLPAIGIFD, _Mapping]]] = ...) -> None: ...
