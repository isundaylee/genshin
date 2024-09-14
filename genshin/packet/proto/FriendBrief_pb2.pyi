from genshin.packet.proto import FriendOnlineState_pb2 as _FriendOnlineState_pb2
from genshin.packet.proto import SocialShowAvatarInfo_pb2 as _SocialShowAvatarInfo_pb2
from genshin.packet.proto import FriendEnterHomeOption_pb2 as _FriendEnterHomeOption_pb2
from genshin.packet.proto import ProfilePicture_pb2 as _ProfilePicture_pb2
from genshin.packet.proto import PlatformType_pb2 as _PlatformType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendBrief(_message.Message):
    __slots__ = ("uid", "nickname", "level", "avatar_id", "world_level", "signature", "online_state", "param", "is_mp_mode_available", "online_id", "last_active_time", "name_card_id", "mp_player_num", "is_chat_no_disturb", "chat_sequence", "remark_name", "show_avatar_info_list", "friend_enter_home_option", "profile_picture", "is_game_source", "is_psn_source", "platform_type", "is_in_duel", "is_duel_observable")
    UID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    WORLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_STATE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    IS_MP_MODE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_CARD_ID_FIELD_NUMBER: _ClassVar[int]
    MP_PLAYER_NUM_FIELD_NUMBER: _ClassVar[int]
    IS_CHAT_NO_DISTURB_FIELD_NUMBER: _ClassVar[int]
    CHAT_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    REMARK_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_AVATAR_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    FRIEND_ENTER_HOME_OPTION_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    IS_GAME_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IS_PSN_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_IN_DUEL_FIELD_NUMBER: _ClassVar[int]
    IS_DUEL_OBSERVABLE_FIELD_NUMBER: _ClassVar[int]
    uid: int
    nickname: str
    level: int
    avatar_id: int
    world_level: int
    signature: str
    online_state: _FriendOnlineState_pb2.FriendOnlineState
    param: int
    is_mp_mode_available: bool
    online_id: str
    last_active_time: int
    name_card_id: int
    mp_player_num: int
    is_chat_no_disturb: bool
    chat_sequence: int
    remark_name: str
    show_avatar_info_list: _containers.RepeatedCompositeFieldContainer[_SocialShowAvatarInfo_pb2.SocialShowAvatarInfo]
    friend_enter_home_option: _FriendEnterHomeOption_pb2.FriendEnterHomeOption
    profile_picture: _ProfilePicture_pb2.ProfilePicture
    is_game_source: bool
    is_psn_source: bool
    platform_type: _PlatformType_pb2.PlatformType
    is_in_duel: bool
    is_duel_observable: bool
    def __init__(self, uid: _Optional[int] = ..., nickname: _Optional[str] = ..., level: _Optional[int] = ..., avatar_id: _Optional[int] = ..., world_level: _Optional[int] = ..., signature: _Optional[str] = ..., online_state: _Optional[_Union[_FriendOnlineState_pb2.FriendOnlineState, str]] = ..., param: _Optional[int] = ..., is_mp_mode_available: bool = ..., online_id: _Optional[str] = ..., last_active_time: _Optional[int] = ..., name_card_id: _Optional[int] = ..., mp_player_num: _Optional[int] = ..., is_chat_no_disturb: bool = ..., chat_sequence: _Optional[int] = ..., remark_name: _Optional[str] = ..., show_avatar_info_list: _Optional[_Iterable[_Union[_SocialShowAvatarInfo_pb2.SocialShowAvatarInfo, _Mapping]]] = ..., friend_enter_home_option: _Optional[_Union[_FriendEnterHomeOption_pb2.FriendEnterHomeOption, str]] = ..., profile_picture: _Optional[_Union[_ProfilePicture_pb2.ProfilePicture, _Mapping]] = ..., is_game_source: bool = ..., is_psn_source: bool = ..., platform_type: _Optional[_Union[_PlatformType_pb2.PlatformType, str]] = ..., is_in_duel: bool = ..., is_duel_observable: bool = ...) -> None: ...
