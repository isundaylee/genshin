from genshin.packet.proto import ActivityInfo_pb2 as _ActivityInfo_pb2
from genshin.packet.proto import Uint32Pair_pb2 as _Uint32Pair_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetActivityInfoRsp(_message.Message):
    __slots__ = ("activity_info_list", "disable_transfer_point_interaction_list", "activated_sale_id_list", "retcode")
    ACTIVITY_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TRANSFER_POINT_INTERACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_SALE_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    activity_info_list: _containers.RepeatedCompositeFieldContainer[_ActivityInfo_pb2.ActivityInfo]
    disable_transfer_point_interaction_list: _containers.RepeatedCompositeFieldContainer[_Uint32Pair_pb2.Uint32Pair]
    activated_sale_id_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    def __init__(self, activity_info_list: _Optional[_Iterable[_Union[_ActivityInfo_pb2.ActivityInfo, _Mapping]]] = ..., disable_transfer_point_interaction_list: _Optional[_Iterable[_Union[_Uint32Pair_pb2.Uint32Pair, _Mapping]]] = ..., activated_sale_id_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ...) -> None: ...
