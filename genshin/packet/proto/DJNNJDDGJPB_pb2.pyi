from genshin.packet.proto import NIEGOBDDJKN_pb2 as _NIEGOBDDJKN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DJNNJDDGJPB(_message.Message):
    __slots__ = ("HNCBGDMHGEA", "DBFGJNBBDKC", "HOINFBDGEFK", "PJABEFAJBGB")
    HNCBGDMHGEA_FIELD_NUMBER: _ClassVar[int]
    DBFGJNBBDKC_FIELD_NUMBER: _ClassVar[int]
    HOINFBDGEFK_FIELD_NUMBER: _ClassVar[int]
    PJABEFAJBGB_FIELD_NUMBER: _ClassVar[int]
    HNCBGDMHGEA: _containers.RepeatedCompositeFieldContainer[_NIEGOBDDJKN_pb2.NIEGOBDDJKN]
    DBFGJNBBDKC: int
    HOINFBDGEFK: int
    PJABEFAJBGB: int
    def __init__(self, HNCBGDMHGEA: _Optional[_Iterable[_Union[_NIEGOBDDJKN_pb2.NIEGOBDDJKN, _Mapping]]] = ..., DBFGJNBBDKC: _Optional[int] = ..., HOINFBDGEFK: _Optional[int] = ..., PJABEFAJBGB: _Optional[int] = ...) -> None: ...
