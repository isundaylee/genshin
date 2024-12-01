from genshin.packet.proto import HLAIBKPEPLK_pb2 as _HLAIBKPEPLK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ENFMOPIEEMA(_message.Message):
    __slots__ = ("GPHHKGMAAEE",)
    class GPHHKGMAAEEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _HLAIBKPEPLK_pb2.HLAIBKPEPLK
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_HLAIBKPEPLK_pb2.HLAIBKPEPLK, _Mapping]] = ...) -> None: ...
    GPHHKGMAAEE_FIELD_NUMBER: _ClassVar[int]
    GPHHKGMAAEE: _containers.MessageMap[int, _HLAIBKPEPLK_pb2.HLAIBKPEPLK]
    def __init__(self, GPHHKGMAAEE: _Optional[_Mapping[int, _HLAIBKPEPLK_pb2.HLAIBKPEPLK]] = ...) -> None: ...
