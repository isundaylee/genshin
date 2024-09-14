from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GadgetGeneralRewardInfo(_message.Message):
    __slots__ = ("resin", "dead_time", "remain_uid_list", "qualify_uid_list", "item_param")
    RESIN_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_FIELD_NUMBER: _ClassVar[int]
    REMAIN_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    QUALIFY_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    ITEM_PARAM_FIELD_NUMBER: _ClassVar[int]
    resin: int
    dead_time: int
    remain_uid_list: _containers.RepeatedScalarFieldContainer[int]
    qualify_uid_list: _containers.RepeatedScalarFieldContainer[int]
    item_param: _ItemParam_pb2.ItemParam
    def __init__(self, resin: _Optional[int] = ..., dead_time: _Optional[int] = ..., remain_uid_list: _Optional[_Iterable[int]] = ..., qualify_uid_list: _Optional[_Iterable[int]] = ..., item_param: _Optional[_Union[_ItemParam_pb2.ItemParam, _Mapping]] = ...) -> None: ...
