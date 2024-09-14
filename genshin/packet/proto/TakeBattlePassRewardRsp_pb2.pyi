from genshin.packet.proto import BattlePassRewardTakeOption_pb2 as _BattlePassRewardTakeOption_pb2
from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeBattlePassRewardRsp(_message.Message):
    __slots__ = ("item_list", "take_option_list", "retcode")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    TAKE_OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    take_option_list: _containers.RepeatedCompositeFieldContainer[_BattlePassRewardTakeOption_pb2.BattlePassRewardTakeOption]
    retcode: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., take_option_list: _Optional[_Iterable[_Union[_BattlePassRewardTakeOption_pb2.BattlePassRewardTakeOption, _Mapping]]] = ..., retcode: _Optional[int] = ...) -> None: ...
