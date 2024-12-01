from genshin.packet.proto import GDMLPOEDPJO_pb2 as _GDMLPOEDPJO_pb2
from genshin.packet.proto import HOFCOAIFPLB_pb2 as _HOFCOAIFPLB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AMEJLDMINEE(_message.Message):
    __slots__ = ("PJEEOONMMDK", "CPIEAINBKDH", "CJGOFEODNAH")
    class CPIEAINBKDHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _HOFCOAIFPLB_pb2.HOFCOAIFPLB
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_HOFCOAIFPLB_pb2.HOFCOAIFPLB, _Mapping]] = ...) -> None: ...
    PJEEOONMMDK_FIELD_NUMBER: _ClassVar[int]
    CPIEAINBKDH_FIELD_NUMBER: _ClassVar[int]
    CJGOFEODNAH_FIELD_NUMBER: _ClassVar[int]
    PJEEOONMMDK: _containers.RepeatedCompositeFieldContainer[_GDMLPOEDPJO_pb2.GDMLPOEDPJO]
    CPIEAINBKDH: _containers.MessageMap[int, _HOFCOAIFPLB_pb2.HOFCOAIFPLB]
    CJGOFEODNAH: _containers.RepeatedCompositeFieldContainer[_GDMLPOEDPJO_pb2.GDMLPOEDPJO]
    def __init__(self, PJEEOONMMDK: _Optional[_Iterable[_Union[_GDMLPOEDPJO_pb2.GDMLPOEDPJO, _Mapping]]] = ..., CPIEAINBKDH: _Optional[_Mapping[int, _HOFCOAIFPLB_pb2.HOFCOAIFPLB]] = ..., CJGOFEODNAH: _Optional[_Iterable[_Union[_GDMLPOEDPJO_pb2.GDMLPOEDPJO, _Mapping]]] = ...) -> None: ...
