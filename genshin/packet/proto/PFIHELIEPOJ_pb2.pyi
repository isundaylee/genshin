from genshin.packet.proto import MNFELHIEBKP_pb2 as _MNFELHIEBKP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PFIHELIEPOJ(_message.Message):
    __slots__ = ("NMOOCJNBEOH", "JMEHMGCPFBO", "BDEFLCDKDBI", "OMENIAMEDCE")
    class NMOOCJNBEOHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _MNFELHIEBKP_pb2.MNFELHIEBKP
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_MNFELHIEBKP_pb2.MNFELHIEBKP, _Mapping]] = ...) -> None: ...
    NMOOCJNBEOH_FIELD_NUMBER: _ClassVar[int]
    JMEHMGCPFBO_FIELD_NUMBER: _ClassVar[int]
    BDEFLCDKDBI_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    NMOOCJNBEOH: _containers.MessageMap[int, _MNFELHIEBKP_pb2.MNFELHIEBKP]
    JMEHMGCPFBO: int
    BDEFLCDKDBI: int
    OMENIAMEDCE: bool
    def __init__(self, NMOOCJNBEOH: _Optional[_Mapping[int, _MNFELHIEBKP_pb2.MNFELHIEBKP]] = ..., JMEHMGCPFBO: _Optional[int] = ..., BDEFLCDKDBI: _Optional[int] = ..., OMENIAMEDCE: bool = ...) -> None: ...
