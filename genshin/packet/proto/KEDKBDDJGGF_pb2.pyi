from genshin.packet.proto import EPANGOOIECN_pb2 as _EPANGOOIECN_pb2
from genshin.packet.proto import BHDOHIGEJAN_pb2 as _BHDOHIGEJAN_pb2
from genshin.packet.proto import CLNAGPOKMIH_pb2 as _CLNAGPOKMIH_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KEDKBDDJGGF(_message.Message):
    __slots__ = ("NKKCADBJEDL", "IOPGOMDHNBA", "APEFOHJKIIK", "EJNINFFFKJP")
    NKKCADBJEDL_FIELD_NUMBER: _ClassVar[int]
    IOPGOMDHNBA_FIELD_NUMBER: _ClassVar[int]
    APEFOHJKIIK_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    NKKCADBJEDL: _EPANGOOIECN_pb2.EPANGOOIECN
    IOPGOMDHNBA: _BHDOHIGEJAN_pb2.BHDOHIGEJAN
    APEFOHJKIIK: _CLNAGPOKMIH_pb2.CLNAGPOKMIH
    EJNINFFFKJP: int
    def __init__(self, NKKCADBJEDL: _Optional[_Union[_EPANGOOIECN_pb2.EPANGOOIECN, _Mapping]] = ..., IOPGOMDHNBA: _Optional[_Union[_BHDOHIGEJAN_pb2.BHDOHIGEJAN, _Mapping]] = ..., APEFOHJKIIK: _Optional[_Union[_CLNAGPOKMIH_pb2.CLNAGPOKMIH, _Mapping]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
