from genshin.packet.proto import IHKLGMIFGMN_pb2 as _IHKLGMIFGMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class POFKPPEILFC(_message.Message):
    __slots__ = ("DMBODNCJOKF", "MODJGAJFAJL", "FBABMDIBFKD")
    class MODJGAJFAJLEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _IHKLGMIFGMN_pb2.IHKLGMIFGMN
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_IHKLGMIFGMN_pb2.IHKLGMIFGMN, _Mapping]] = ...) -> None: ...
    DMBODNCJOKF_FIELD_NUMBER: _ClassVar[int]
    MODJGAJFAJL_FIELD_NUMBER: _ClassVar[int]
    FBABMDIBFKD_FIELD_NUMBER: _ClassVar[int]
    DMBODNCJOKF: _containers.RepeatedScalarFieldContainer[int]
    MODJGAJFAJL: _containers.MessageMap[int, _IHKLGMIFGMN_pb2.IHKLGMIFGMN]
    FBABMDIBFKD: int
    def __init__(self, DMBODNCJOKF: _Optional[_Iterable[int]] = ..., MODJGAJFAJL: _Optional[_Mapping[int, _IHKLGMIFGMN_pb2.IHKLGMIFGMN]] = ..., FBABMDIBFKD: _Optional[int] = ...) -> None: ...
