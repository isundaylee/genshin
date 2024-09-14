from genshin.packet.proto import Birthday_pb2 as _Birthday_pb2
from genshin.packet.proto import FriendOnlineState_pb2 as _FriendOnlineState_pb2
from genshin.packet.proto import SocialShowAvatarInfo_pb2 as _SocialShowAvatarInfo_pb2
from genshin.packet.proto import FriendEnterHomeOption_pb2 as _FriendEnterHomeOption_pb2
from genshin.packet.proto import ProfilePicture_pb2 as _ProfilePicture_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SocialDetail(_message.Message):
    __slots__ = ("uid", "nickname", "level", "avatar_id", "signature", "birthday", "world_level", "reserved_list", "online_state", "param", "is_friend", "is_mp_mode_available", "online_id", "name_card_id", "is_in_blacklist", "is_chat_no_disturb", "remark_name", "finish_achievement_num", "tower_floor_index", "tower_level_index", "is_show_avatar", "show_avatar_info_list", "show_name_card_id_list", "friend_enter_home_option", "profile_picture", "ip_code", "CMOBLNACDIE", "GEGBOECJJMO", "MBOLLDBJPCP", "is_show_constellation_num", "FLMFEMCAFHB", "MOBMAJIJJGL")
    UID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    WORLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RESERVED_LIST_FIELD_NUMBER: _ClassVar[int]
    ONLINE_STATE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    IS_FRIEND_FIELD_NUMBER: _ClassVar[int]
    IS_MP_MODE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_CARD_ID_FIELD_NUMBER: _ClassVar[int]
    IS_IN_BLACKLIST_FIELD_NUMBER: _ClassVar[int]
    IS_CHAT_NO_DISTURB_FIELD_NUMBER: _ClassVar[int]
    REMARK_NAME_FIELD_NUMBER: _ClassVar[int]
    FINISH_ACHIEVEMENT_NUM_FIELD_NUMBER: _ClassVar[int]
    TOWER_FLOOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    TOWER_LEVEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_AVATAR_FIELD_NUMBER: _ClassVar[int]
    SHOW_AVATAR_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    SHOW_NAME_CARD_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    FRIEND_ENTER_HOME_OPTION_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    IP_CODE_FIELD_NUMBER: _ClassVar[int]
    CMOBLNACDIE_FIELD_NUMBER: _ClassVar[int]
    GEGBOECJJMO_FIELD_NUMBER: _ClassVar[int]
    MBOLLDBJPCP_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_CONSTELLATION_NUM_FIELD_NUMBER: _ClassVar[int]
    FLMFEMCAFHB_FIELD_NUMBER: _ClassVar[int]
    MOBMAJIJJGL_FIELD_NUMBER: _ClassVar[int]
    uid: int
    nickname: str
    level: int
    avatar_id: int
    signature: str
    birthday: _Birthday_pb2.Birthday
    world_level: int
    reserved_list: _containers.RepeatedScalarFieldContainer[int]
    online_state: _FriendOnlineState_pb2.FriendOnlineState
    param: int
    is_friend: bool
    is_mp_mode_available: bool
    online_id: str
    name_card_id: int
    is_in_blacklist: bool
    is_chat_no_disturb: bool
    remark_name: str
    finish_achievement_num: int
    tower_floor_index: int
    tower_level_index: int
    is_show_avatar: bool
    show_avatar_info_list: _containers.RepeatedCompositeFieldContainer[_SocialShowAvatarInfo_pb2.SocialShowAvatarInfo]
    show_name_card_id_list: _containers.RepeatedScalarFieldContainer[int]
    friend_enter_home_option: _FriendEnterHomeOption_pb2.FriendEnterHomeOption
    profile_picture: _ProfilePicture_pb2.ProfilePicture
    ip_code: str
    CMOBLNACDIE: int
    GEGBOECJJMO: int
    MBOLLDBJPCP: int
    is_show_constellation_num: bool
    FLMFEMCAFHB: int
    MOBMAJIJJGL: int
    def __init__(self, uid: _Optional[int] = ..., nickname: _Optional[str] = ..., level: _Optional[int] = ..., avatar_id: _Optional[int] = ..., signature: _Optional[str] = ..., birthday: _Optional[_Union[_Birthday_pb2.Birthday, _Mapping]] = ..., world_level: _Optional[int] = ..., reserved_list: _Optional[_Iterable[int]] = ..., online_state: _Optional[_Union[_FriendOnlineState_pb2.FriendOnlineState, str]] = ..., param: _Optional[int] = ..., is_friend: bool = ..., is_mp_mode_available: bool = ..., online_id: _Optional[str] = ..., name_card_id: _Optional[int] = ..., is_in_blacklist: bool = ..., is_chat_no_disturb: bool = ..., remark_name: _Optional[str] = ..., finish_achievement_num: _Optional[int] = ..., tower_floor_index: _Optional[int] = ..., tower_level_index: _Optional[int] = ..., is_show_avatar: bool = ..., show_avatar_info_list: _Optional[_Iterable[_Union[_SocialShowAvatarInfo_pb2.SocialShowAvatarInfo, _Mapping]]] = ..., show_name_card_id_list: _Optional[_Iterable[int]] = ..., friend_enter_home_option: _Optional[_Union[_FriendEnterHomeOption_pb2.FriendEnterHomeOption, str]] = ..., profile_picture: _Optional[_Union[_ProfilePicture_pb2.ProfilePicture, _Mapping]] = ..., ip_code: _Optional[str] = ..., CMOBLNACDIE: _Optional[int] = ..., GEGBOECJJMO: _Optional[int] = ..., MBOLLDBJPCP: _Optional[int] = ..., is_show_constellation_num: bool = ..., FLMFEMCAFHB: _Optional[int] = ..., MOBMAJIJJGL: _Optional[int] = ...) -> None: ...
