from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from genshin.packet.proto import ForgeQueueManipulateType_pb2 as _ForgeQueueManipulateType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForgeQueueManipulateRsp(_message.Message):
    __slots__ = ("output_item_list", "extra_output_item_list", "manipulate_type", "return_item_list", "retcode")
    OUTPUT_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    EXTRA_OUTPUT_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    MANIPULATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETURN_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    output_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    extra_output_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    manipulate_type: _ForgeQueueManipulateType_pb2.ForgeQueueManipulateType
    return_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    retcode: int
    def __init__(self, output_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., extra_output_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., manipulate_type: _Optional[_Union[_ForgeQueueManipulateType_pb2.ForgeQueueManipulateType, str]] = ..., return_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., retcode: _Optional[int] = ...) -> None: ...
