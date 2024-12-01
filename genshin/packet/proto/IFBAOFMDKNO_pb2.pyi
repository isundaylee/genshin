from genshin.packet.proto import GJBKFOPDCGK_pb2 as _GJBKFOPDCGK_pb2
from genshin.packet.proto import NBDHFHKMLFD_pb2 as _NBDHFHKMLFD_pb2
from genshin.packet.proto import PEELKMKJKPP_pb2 as _PEELKMKJKPP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IFBAOFMDKNO(_message.Message):
    __slots__ = ("HILLLCLAILE", "FHMDOPHEELD", "IMIOGMDOKCB")
    HILLLCLAILE_FIELD_NUMBER: _ClassVar[int]
    FHMDOPHEELD_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    HILLLCLAILE: _containers.RepeatedCompositeFieldContainer[_GJBKFOPDCGK_pb2.GJBKFOPDCGK]
    FHMDOPHEELD: _NBDHFHKMLFD_pb2.NBDHFHKMLFD
    IMIOGMDOKCB: _PEELKMKJKPP_pb2.PEELKMKJKPP
    def __init__(self, HILLLCLAILE: _Optional[_Iterable[_Union[_GJBKFOPDCGK_pb2.GJBKFOPDCGK, _Mapping]]] = ..., FHMDOPHEELD: _Optional[_Union[_NBDHFHKMLFD_pb2.NBDHFHKMLFD, _Mapping]] = ..., IMIOGMDOKCB: _Optional[_Union[_PEELKMKJKPP_pb2.PEELKMKJKPP, str]] = ...) -> None: ...
