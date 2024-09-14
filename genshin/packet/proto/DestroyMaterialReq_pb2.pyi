from genshin.packet.proto import MaterialInfo_pb2 as _MaterialInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DestroyMaterialReq(_message.Message):
    __slots__ = ("material_list",)
    MATERIAL_LIST_FIELD_NUMBER: _ClassVar[int]
    material_list: _containers.RepeatedCompositeFieldContainer[_MaterialInfo_pb2.MaterialInfo]
    def __init__(self, material_list: _Optional[_Iterable[_Union[_MaterialInfo_pb2.MaterialInfo, _Mapping]]] = ...) -> None: ...
