from genshin.packet.proto import CustomCommonNodeInfo_pb2 as _CustomCommonNodeInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomGadgetTreeInfo(_message.Message):
    __slots__ = ("node_list",)
    NODE_LIST_FIELD_NUMBER: _ClassVar[int]
    node_list: _containers.RepeatedCompositeFieldContainer[_CustomCommonNodeInfo_pb2.CustomCommonNodeInfo]
    def __init__(self, node_list: _Optional[_Iterable[_Union[_CustomCommonNodeInfo_pb2.CustomCommonNodeInfo, _Mapping]]] = ...) -> None: ...
