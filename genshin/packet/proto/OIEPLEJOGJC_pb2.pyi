from genshin.packet.proto import MINGHCPOBNG_pb2 as _MINGHCPOBNG_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OIEPLEJOGJC(_message.Message):
    __slots__ = ("NGANCEICGHC", "OMENIAMEDCE")
    NGANCEICGHC_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    NGANCEICGHC: _MINGHCPOBNG_pb2.MINGHCPOBNG
    OMENIAMEDCE: bool
    def __init__(self, NGANCEICGHC: _Optional[_Union[_MINGHCPOBNG_pb2.MINGHCPOBNG, _Mapping]] = ..., OMENIAMEDCE: bool = ...) -> None: ...
