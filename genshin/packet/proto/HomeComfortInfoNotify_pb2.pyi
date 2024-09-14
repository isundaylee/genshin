from genshin.packet.proto import HomeModuleComfortInfo_pb2 as _HomeModuleComfortInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeComfortInfoNotify(_message.Message):
    __slots__ = ("module_info_list",)
    MODULE_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    module_info_list: _containers.RepeatedCompositeFieldContainer[_HomeModuleComfortInfo_pb2.HomeModuleComfortInfo]
    def __init__(self, module_info_list: _Optional[_Iterable[_Union[_HomeModuleComfortInfo_pb2.HomeModuleComfortInfo, _Mapping]]] = ...) -> None: ...
