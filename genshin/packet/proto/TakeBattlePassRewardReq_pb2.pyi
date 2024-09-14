from genshin.packet.proto import BattlePassRewardTakeOption_pb2 as _BattlePassRewardTakeOption_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeBattlePassRewardReq(_message.Message):
    __slots__ = ("take_option_list",)
    TAKE_OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    take_option_list: _containers.RepeatedCompositeFieldContainer[_BattlePassRewardTakeOption_pb2.BattlePassRewardTakeOption]
    def __init__(self, take_option_list: _Optional[_Iterable[_Union[_BattlePassRewardTakeOption_pb2.BattlePassRewardTakeOption, _Mapping]]] = ...) -> None: ...
