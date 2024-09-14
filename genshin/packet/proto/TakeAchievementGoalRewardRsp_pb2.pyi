from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeAchievementGoalRewardRsp(_message.Message):
    __slots__ = ("item_list", "id_list", "retcode")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    ID_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    id_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., id_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ...) -> None: ...
