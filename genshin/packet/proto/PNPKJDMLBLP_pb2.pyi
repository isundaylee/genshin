from genshin.packet.proto import BHDNHBGEAEH_pb2 as _BHDNHBGEAEH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PNPKJDMLBLP(_message.Message):
    __slots__ = ("IDDOABLMBLP",)
    class IDDOABLMBLPEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _BHDNHBGEAEH_pb2.BHDNHBGEAEH
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_BHDNHBGEAEH_pb2.BHDNHBGEAEH, _Mapping]] = ...) -> None: ...
    IDDOABLMBLP_FIELD_NUMBER: _ClassVar[int]
    IDDOABLMBLP: _containers.MessageMap[int, _BHDNHBGEAEH_pb2.BHDNHBGEAEH]
    def __init__(self, IDDOABLMBLP: _Optional[_Mapping[int, _BHDNHBGEAEH_pb2.BHDNHBGEAEH]] = ...) -> None: ...
