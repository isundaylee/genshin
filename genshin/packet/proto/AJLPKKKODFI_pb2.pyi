from genshin.packet.proto import BJDOJCHBBGM_pb2 as _BJDOJCHBBGM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AJLPKKKODFI(_message.Message):
    __slots__ = ("HJOBNJHNPNL", "BIABFNLMMFE", "ADNCOLNBCFN", "IADFGKJCIDE")
    HJOBNJHNPNL_FIELD_NUMBER: _ClassVar[int]
    BIABFNLMMFE_FIELD_NUMBER: _ClassVar[int]
    ADNCOLNBCFN_FIELD_NUMBER: _ClassVar[int]
    IADFGKJCIDE_FIELD_NUMBER: _ClassVar[int]
    HJOBNJHNPNL: _containers.RepeatedCompositeFieldContainer[_BJDOJCHBBGM_pb2.BJDOJCHBBGM]
    BIABFNLMMFE: int
    ADNCOLNBCFN: bool
    IADFGKJCIDE: int
    def __init__(self, HJOBNJHNPNL: _Optional[_Iterable[_Union[_BJDOJCHBBGM_pb2.BJDOJCHBBGM, _Mapping]]] = ..., BIABFNLMMFE: _Optional[int] = ..., ADNCOLNBCFN: bool = ..., IADFGKJCIDE: _Optional[int] = ...) -> None: ...
