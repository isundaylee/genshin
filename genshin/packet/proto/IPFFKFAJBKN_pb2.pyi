from genshin.packet.proto import ENOFBCMAAJL_pb2 as _ENOFBCMAAJL_pb2
from genshin.packet.proto import KGBKIFDBEPC_pb2 as _KGBKIFDBEPC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IPFFKFAJBKN(_message.Message):
    __slots__ = ("PMJBOEGCPMH", "GKKAMPPDFIB")
    class GKKAMPPDFIBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _KGBKIFDBEPC_pb2.KGBKIFDBEPC
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_KGBKIFDBEPC_pb2.KGBKIFDBEPC, _Mapping]] = ...) -> None: ...
    PMJBOEGCPMH_FIELD_NUMBER: _ClassVar[int]
    GKKAMPPDFIB_FIELD_NUMBER: _ClassVar[int]
    PMJBOEGCPMH: _containers.RepeatedCompositeFieldContainer[_ENOFBCMAAJL_pb2.ENOFBCMAAJL]
    GKKAMPPDFIB: _containers.MessageMap[int, _KGBKIFDBEPC_pb2.KGBKIFDBEPC]
    def __init__(self, PMJBOEGCPMH: _Optional[_Iterable[_Union[_ENOFBCMAAJL_pb2.ENOFBCMAAJL, _Mapping]]] = ..., GKKAMPPDFIB: _Optional[_Mapping[int, _KGBKIFDBEPC_pb2.KGBKIFDBEPC]] = ...) -> None: ...
