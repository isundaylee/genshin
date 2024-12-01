from genshin.packet.proto import HPKNPBFCPPD_pb2 as _HPKNPBFCPPD_pb2
from genshin.packet.proto import HBLKLJKHKOO_pb2 as _HBLKLJKHKOO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JKBIKPKNBIE(_message.Message):
    __slots__ = ("GPGMGLNANIB", "DDPFMKJFPAK", "MPFLDFDOGAI", "NMIKCMLKNDM")
    class DDPFMKJFPAKEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _HBLKLJKHKOO_pb2.HBLKLJKHKOO
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_HBLKLJKHKOO_pb2.HBLKLJKHKOO, _Mapping]] = ...) -> None: ...
    GPGMGLNANIB_FIELD_NUMBER: _ClassVar[int]
    DDPFMKJFPAK_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    NMIKCMLKNDM_FIELD_NUMBER: _ClassVar[int]
    GPGMGLNANIB: _HPKNPBFCPPD_pb2.HPKNPBFCPPD
    DDPFMKJFPAK: _containers.MessageMap[int, _HBLKLJKHKOO_pb2.HBLKLJKHKOO]
    MPFLDFDOGAI: bool
    NMIKCMLKNDM: int
    def __init__(self, GPGMGLNANIB: _Optional[_Union[_HPKNPBFCPPD_pb2.HPKNPBFCPPD, _Mapping]] = ..., DDPFMKJFPAK: _Optional[_Mapping[int, _HBLKLJKHKOO_pb2.HBLKLJKHKOO]] = ..., MPFLDFDOGAI: bool = ..., NMIKCMLKNDM: _Optional[int] = ...) -> None: ...
