from genshin.packet.proto import BattlePassRewardTag_pb2 as _BattlePassRewardTag_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassRewardTakeOption(_message.Message):
    __slots__ = ("option_idx", "tag")
    OPTION_IDX_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    option_idx: int
    tag: _BattlePassRewardTag_pb2.BattlePassRewardTag
    def __init__(self, option_idx: _Optional[int] = ..., tag: _Optional[_Union[_BattlePassRewardTag_pb2.BattlePassRewardTag, _Mapping]] = ...) -> None: ...
