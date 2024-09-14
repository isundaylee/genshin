from genshin.packet.proto import FriendEnterHomeOption_pb2 as _FriendEnterHomeOption_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerHomeCompInfo(_message.Message):
    __slots__ = ("friend_enter_home_option", "seen_module_id_list", "unlocked_module_id_list", "levelup_reward_got_level_list")
    FRIEND_ENTER_HOME_OPTION_FIELD_NUMBER: _ClassVar[int]
    SEEN_MODULE_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_MODULE_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    LEVELUP_REWARD_GOT_LEVEL_LIST_FIELD_NUMBER: _ClassVar[int]
    friend_enter_home_option: _FriendEnterHomeOption_pb2.FriendEnterHomeOption
    seen_module_id_list: _containers.RepeatedScalarFieldContainer[int]
    unlocked_module_id_list: _containers.RepeatedScalarFieldContainer[int]
    levelup_reward_got_level_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, friend_enter_home_option: _Optional[_Union[_FriendEnterHomeOption_pb2.FriendEnterHomeOption, str]] = ..., seen_module_id_list: _Optional[_Iterable[int]] = ..., unlocked_module_id_list: _Optional[_Iterable[int]] = ..., levelup_reward_got_level_list: _Optional[_Iterable[int]] = ...) -> None: ...
