from genshin.packet.proto import AvatarRenameInfo_pb2 as _AvatarRenameInfo_pb2
from genshin.packet.proto import AvatarInfo_pb2 as _AvatarInfo_pb2
from genshin.packet.proto import AvatarTeam_pb2 as _AvatarTeam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarDataNotify(_message.Message):
    __slots__ = ("CPEAJKCGPIO", "PBIOIIFOAPA", "avatar_rename_list", "avatar_list", "temp_avatar_guid_list", "OPHDOKOFIHO", "KPIGEEJAMHM", "avatar_team_map", "choose_avatar_guid", "cur_avatar_team_id")
    class AvatarTeamMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AvatarTeam_pb2.AvatarTeam
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AvatarTeam_pb2.AvatarTeam, _Mapping]] = ...) -> None: ...
    CPEAJKCGPIO_FIELD_NUMBER: _ClassVar[int]
    PBIOIIFOAPA_FIELD_NUMBER: _ClassVar[int]
    AVATAR_RENAME_LIST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_LIST_FIELD_NUMBER: _ClassVar[int]
    TEMP_AVATAR_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    OPHDOKOFIHO_FIELD_NUMBER: _ClassVar[int]
    KPIGEEJAMHM_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TEAM_MAP_FIELD_NUMBER: _ClassVar[int]
    CHOOSE_AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    CUR_AVATAR_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CPEAJKCGPIO: _containers.RepeatedScalarFieldContainer[int]
    PBIOIIFOAPA: _containers.RepeatedScalarFieldContainer[int]
    avatar_rename_list: _containers.RepeatedCompositeFieldContainer[_AvatarRenameInfo_pb2.AvatarRenameInfo]
    avatar_list: _containers.RepeatedCompositeFieldContainer[_AvatarInfo_pb2.AvatarInfo]
    temp_avatar_guid_list: _containers.RepeatedScalarFieldContainer[int]
    OPHDOKOFIHO: _containers.RepeatedScalarFieldContainer[int]
    KPIGEEJAMHM: _containers.RepeatedScalarFieldContainer[int]
    avatar_team_map: _containers.MessageMap[int, _AvatarTeam_pb2.AvatarTeam]
    choose_avatar_guid: int
    cur_avatar_team_id: int
    def __init__(self, CPEAJKCGPIO: _Optional[_Iterable[int]] = ..., PBIOIIFOAPA: _Optional[_Iterable[int]] = ..., avatar_rename_list: _Optional[_Iterable[_Union[_AvatarRenameInfo_pb2.AvatarRenameInfo, _Mapping]]] = ..., avatar_list: _Optional[_Iterable[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]]] = ..., temp_avatar_guid_list: _Optional[_Iterable[int]] = ..., OPHDOKOFIHO: _Optional[_Iterable[int]] = ..., KPIGEEJAMHM: _Optional[_Iterable[int]] = ..., avatar_team_map: _Optional[_Mapping[int, _AvatarTeam_pb2.AvatarTeam]] = ..., choose_avatar_guid: _Optional[int] = ..., cur_avatar_team_id: _Optional[int] = ...) -> None: ...
