from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from genshin.packet.proto import FurnitureMakeSlot_pb2 as _FurnitureMakeSlot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeFurnitureMakeRsp(_message.Message):
    __slots__ = ("return_item_list", "furniture_make_slot", "output_item_list", "make_id", "retcode")
    RETURN_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_MAKE_SLOT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    MAKE_ID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    return_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    furniture_make_slot: _FurnitureMakeSlot_pb2.FurnitureMakeSlot
    output_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    make_id: int
    retcode: int
    def __init__(self, return_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., furniture_make_slot: _Optional[_Union[_FurnitureMakeSlot_pb2.FurnitureMakeSlot, _Mapping]] = ..., output_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., make_id: _Optional[int] = ..., retcode: _Optional[int] = ...) -> None: ...
