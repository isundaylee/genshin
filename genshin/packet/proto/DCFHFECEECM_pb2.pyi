from genshin.packet.proto import ALGFOHHNNOD_pb2 as _ALGFOHHNNOD_pb2
from genshin.packet.proto import MIFIKPOHMNG_pb2 as _MIFIKPOHMNG_pb2
from genshin.packet.proto import OPLPJLCPJDO_pb2 as _OPLPJLCPJDO_pb2
from genshin.packet.proto import DDAPMCMNFCD_pb2 as _DDAPMCMNFCD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DCFHFECEECM(_message.Message):
    __slots__ = ("KPLGKJKFJDN", "ABGCDBHMOJL", "HDJFKPNLNJH", "HMECAECDCJN")
    KPLGKJKFJDN_FIELD_NUMBER: _ClassVar[int]
    ABGCDBHMOJL_FIELD_NUMBER: _ClassVar[int]
    HDJFKPNLNJH_FIELD_NUMBER: _ClassVar[int]
    HMECAECDCJN_FIELD_NUMBER: _ClassVar[int]
    KPLGKJKFJDN: _ALGFOHHNNOD_pb2.ALGFOHHNNOD
    ABGCDBHMOJL: _containers.RepeatedCompositeFieldContainer[_MIFIKPOHMNG_pb2.MIFIKPOHMNG]
    HDJFKPNLNJH: _OPLPJLCPJDO_pb2.OPLPJLCPJDO
    HMECAECDCJN: _DDAPMCMNFCD_pb2.DDAPMCMNFCD
    def __init__(self, KPLGKJKFJDN: _Optional[_Union[_ALGFOHHNNOD_pb2.ALGFOHHNNOD, _Mapping]] = ..., ABGCDBHMOJL: _Optional[_Iterable[_Union[_MIFIKPOHMNG_pb2.MIFIKPOHMNG, _Mapping]]] = ..., HDJFKPNLNJH: _Optional[_Union[_OPLPJLCPJDO_pb2.OPLPJLCPJDO, _Mapping]] = ..., HMECAECDCJN: _Optional[_Union[_DDAPMCMNFCD_pb2.DDAPMCMNFCD, _Mapping]] = ...) -> None: ...
