from genshin.packet.proto import HPDPKLFDMCE_pb2 as _HPDPKLFDMCE_pb2
from genshin.packet.proto import PKAPHPKFAFJ_pb2 as _PKAPHPKFAFJ_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MMPJAELAFGM(_message.Message):
    __slots__ = ("EDJLNGFGLCP", "MNPOIILNKOB", "EJNINFFFKJP")
    EDJLNGFGLCP_FIELD_NUMBER: _ClassVar[int]
    MNPOIILNKOB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    EDJLNGFGLCP: _HPDPKLFDMCE_pb2.HPDPKLFDMCE
    MNPOIILNKOB: _PKAPHPKFAFJ_pb2.PKAPHPKFAFJ
    EJNINFFFKJP: int
    def __init__(self, EDJLNGFGLCP: _Optional[_Union[_HPDPKLFDMCE_pb2.HPDPKLFDMCE, _Mapping]] = ..., MNPOIILNKOB: _Optional[_Union[_PKAPHPKFAFJ_pb2.PKAPHPKFAFJ, _Mapping]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
