from genshin.packet.proto import PNHDMGCFEPK_pb2 as _PNHDMGCFEPK_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HGMBBCIPMGG(_message.Message):
    __slots__ = ("NGANCEICGHC", "FFHPDCIBKOD")
    NGANCEICGHC_FIELD_NUMBER: _ClassVar[int]
    FFHPDCIBKOD_FIELD_NUMBER: _ClassVar[int]
    NGANCEICGHC: _PNHDMGCFEPK_pb2.PNHDMGCFEPK
    FFHPDCIBKOD: int
    def __init__(self, NGANCEICGHC: _Optional[_Union[_PNHDMGCFEPK_pb2.PNHDMGCFEPK, _Mapping]] = ..., FFHPDCIBKOD: _Optional[int] = ...) -> None: ...
