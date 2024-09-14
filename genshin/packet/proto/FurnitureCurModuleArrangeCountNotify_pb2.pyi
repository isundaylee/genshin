from genshin.packet.proto import Uint32Pair_pb2 as _Uint32Pair_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FurnitureCurModuleArrangeCountNotify(_message.Message):
    __slots__ = ("furniture_arrange_count_list",)
    FURNITURE_ARRANGE_COUNT_LIST_FIELD_NUMBER: _ClassVar[int]
    furniture_arrange_count_list: _containers.RepeatedCompositeFieldContainer[_Uint32Pair_pb2.Uint32Pair]
    def __init__(self, furniture_arrange_count_list: _Optional[_Iterable[_Union[_Uint32Pair_pb2.Uint32Pair, _Mapping]]] = ...) -> None: ...
