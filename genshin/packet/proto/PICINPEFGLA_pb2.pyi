from genshin.packet.proto import ABENCJFJIFL_pb2 as _ABENCJFJIFL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PICINPEFGLA(_message.Message):
    __slots__ = ("NGANCEICGHC", "FFHPDCIBKOD", "OMENIAMEDCE", "LHMDBBFAIFM")
    NGANCEICGHC_FIELD_NUMBER: _ClassVar[int]
    FFHPDCIBKOD_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    LHMDBBFAIFM_FIELD_NUMBER: _ClassVar[int]
    NGANCEICGHC: _ABENCJFJIFL_pb2.ABENCJFJIFL
    FFHPDCIBKOD: int
    OMENIAMEDCE: bool
    LHMDBBFAIFM: int
    def __init__(self, NGANCEICGHC: _Optional[_Union[_ABENCJFJIFL_pb2.ABENCJFJIFL, _Mapping]] = ..., FFHPDCIBKOD: _Optional[int] = ..., OMENIAMEDCE: bool = ..., LHMDBBFAIFM: _Optional[int] = ...) -> None: ...
