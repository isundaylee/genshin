from genshin.packet.proto import NNGGBCFBFAJ_pb2 as _NNGGBCFBFAJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HBPJOOKKEJM(_message.Message):
    __slots__ = ("EMEDJDNNGJI", "PENKDNOOOHF", "OJHCPPEHHKG", "OAPKMMMAJLG", "DPJGKAGIAOH")
    class PENKDNOOOHFEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class OAPKMMMAJLGEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _NNGGBCFBFAJ_pb2.NNGGBCFBFAJ
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_NNGGBCFBFAJ_pb2.NNGGBCFBFAJ, _Mapping]] = ...) -> None: ...
    EMEDJDNNGJI_FIELD_NUMBER: _ClassVar[int]
    PENKDNOOOHF_FIELD_NUMBER: _ClassVar[int]
    OJHCPPEHHKG_FIELD_NUMBER: _ClassVar[int]
    OAPKMMMAJLG_FIELD_NUMBER: _ClassVar[int]
    DPJGKAGIAOH_FIELD_NUMBER: _ClassVar[int]
    EMEDJDNNGJI: _containers.RepeatedScalarFieldContainer[int]
    PENKDNOOOHF: _containers.ScalarMap[int, int]
    OJHCPPEHHKG: _containers.RepeatedScalarFieldContainer[int]
    OAPKMMMAJLG: _containers.MessageMap[int, _NNGGBCFBFAJ_pb2.NNGGBCFBFAJ]
    DPJGKAGIAOH: int
    def __init__(self, EMEDJDNNGJI: _Optional[_Iterable[int]] = ..., PENKDNOOOHF: _Optional[_Mapping[int, int]] = ..., OJHCPPEHHKG: _Optional[_Iterable[int]] = ..., OAPKMMMAJLG: _Optional[_Mapping[int, _NNGGBCFBFAJ_pb2.NNGGBCFBFAJ]] = ..., DPJGKAGIAOH: _Optional[int] = ...) -> None: ...
