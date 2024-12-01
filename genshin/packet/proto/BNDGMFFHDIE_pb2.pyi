from genshin.packet.proto import BBICGHBHCBA_pb2 as _BBICGHBHCBA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BNDGMFFHDIE(_message.Message):
    __slots__ = ("JJKEJDKMJLG", "FBPGMONGMJH", "LABBIMKCLJE", "JFLLLBICCIH", "LKCLOGBOOCF", "DJAIIDLDAJM")
    class JJKEJDKMJLGEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class FBPGMONGMJHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    JJKEJDKMJLG_FIELD_NUMBER: _ClassVar[int]
    FBPGMONGMJH_FIELD_NUMBER: _ClassVar[int]
    LABBIMKCLJE_FIELD_NUMBER: _ClassVar[int]
    JFLLLBICCIH_FIELD_NUMBER: _ClassVar[int]
    LKCLOGBOOCF_FIELD_NUMBER: _ClassVar[int]
    DJAIIDLDAJM_FIELD_NUMBER: _ClassVar[int]
    JJKEJDKMJLG: _containers.ScalarMap[int, int]
    FBPGMONGMJH: _containers.ScalarMap[int, int]
    LABBIMKCLJE: _BBICGHBHCBA_pb2.BBICGHBHCBA
    JFLLLBICCIH: _containers.RepeatedCompositeFieldContainer[_BBICGHBHCBA_pb2.BBICGHBHCBA]
    LKCLOGBOOCF: int
    DJAIIDLDAJM: int
    def __init__(self, JJKEJDKMJLG: _Optional[_Mapping[int, int]] = ..., FBPGMONGMJH: _Optional[_Mapping[int, int]] = ..., LABBIMKCLJE: _Optional[_Union[_BBICGHBHCBA_pb2.BBICGHBHCBA, _Mapping]] = ..., JFLLLBICCIH: _Optional[_Iterable[_Union[_BBICGHBHCBA_pb2.BBICGHBHCBA, _Mapping]]] = ..., LKCLOGBOOCF: _Optional[int] = ..., DJAIIDLDAJM: _Optional[int] = ...) -> None: ...
