from genshin.packet.proto import HOFCOAIFPLB_pb2 as _HOFCOAIFPLB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IPDFPEJJFJL(_message.Message):
    __slots__ = ("CPIEAINBKDH",)
    class CPIEAINBKDHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _HOFCOAIFPLB_pb2.HOFCOAIFPLB
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_HOFCOAIFPLB_pb2.HOFCOAIFPLB, _Mapping]] = ...) -> None: ...
    CPIEAINBKDH_FIELD_NUMBER: _ClassVar[int]
    CPIEAINBKDH: _containers.MessageMap[int, _HOFCOAIFPLB_pb2.HOFCOAIFPLB]
    def __init__(self, CPIEAINBKDH: _Optional[_Mapping[int, _HOFCOAIFPLB_pb2.HOFCOAIFPLB]] = ...) -> None: ...
