from genshin.packet.proto import GadgetBornType_pb2 as _GadgetBornType_pb2
from genshin.packet.proto import PlatformInfo_pb2 as _PlatformInfo_pb2
from genshin.packet.proto import GadgetPlayInfo_pb2 as _GadgetPlayInfo_pb2
from genshin.packet.proto import GatherGadgetInfo_pb2 as _GatherGadgetInfo_pb2
from genshin.packet.proto import WorktopInfo_pb2 as _WorktopInfo_pb2
from genshin.packet.proto import ClientGadgetInfo_pb2 as _ClientGadgetInfo_pb2
from genshin.packet.proto import WeatherInfo_pb2 as _WeatherInfo_pb2
from genshin.packet.proto import AbilityGadgetInfo_pb2 as _AbilityGadgetInfo_pb2
from genshin.packet.proto import StatueGadgetInfo_pb2 as _StatueGadgetInfo_pb2
from genshin.packet.proto import BossChestInfo_pb2 as _BossChestInfo_pb2
from genshin.packet.proto import BlossomChestInfo_pb2 as _BlossomChestInfo_pb2
from genshin.packet.proto import MpPlayRewardInfo_pb2 as _MpPlayRewardInfo_pb2
from genshin.packet.proto import GadgetGeneralRewardInfo_pb2 as _GadgetGeneralRewardInfo_pb2
from genshin.packet.proto import OfferingInfo_pb2 as _OfferingInfo_pb2
from genshin.packet.proto import FoundationInfo_pb2 as _FoundationInfo_pb2
from genshin.packet.proto import VehicleInfo_pb2 as _VehicleInfo_pb2
from genshin.packet.proto import EchoShellInfo_pb2 as _EchoShellInfo_pb2
from genshin.packet.proto import ScreenInfo_pb2 as _ScreenInfo_pb2
from genshin.packet.proto import FishPoolInfo_pb2 as _FishPoolInfo_pb2
from genshin.packet.proto import CustomGadgetTreeInfo_pb2 as _CustomGadgetTreeInfo_pb2
from genshin.packet.proto import RoguelikeGadgetInfo_pb2 as _RoguelikeGadgetInfo_pb2
from genshin.packet.proto import NightCrowGadgetInfo_pb2 as _NightCrowGadgetInfo_pb2
from genshin.packet.proto import DeshretObeliskGadgetInfo_pb2 as _DeshretObeliskGadgetInfo_pb2
from genshin.packet.proto import CoinCollectOperatorInfo_pb2 as _CoinCollectOperatorInfo_pb2
from genshin.packet.proto import TrifleGadget_pb2 as _TrifleGadget_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneGadgetInfo(_message.Message):
    __slots__ = ("gadget_id", "group_id", "config_id", "owner_entity_id", "born_type", "gadget_state", "gadget_type", "is_show_cutscene", "authority_peer_id", "is_enable_interact", "interact_id", "mark_flag", "prop_owner_entity_id", "platform", "interact_uid_list", "draft_id", "gadget_talk_state", "init_pose_id", "play_info", "gather_gadget", "worktop", "client_gadget", "weather", "ability_gadget", "statue_gadget", "boss_chest", "blossom_chest", "mp_play_reward", "general_reward", "offering_info", "foundation_info", "vehicle_info", "shell_info", "screen_info", "fish_pool_info", "custom_gadget_tree_info", "roguelike_gadget_info", "night_crow_gadget_info", "deshret_obelisk_gadget_info", "coin_collect_operator_info", "trifle_gadget")
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    BORN_TYPE_FIELD_NUMBER: _ClassVar[int]
    GADGET_STATE_FIELD_NUMBER: _ClassVar[int]
    GADGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_CUTSCENE_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLE_INTERACT_FIELD_NUMBER: _ClassVar[int]
    INTERACT_ID_FIELD_NUMBER: _ClassVar[int]
    MARK_FLAG_FIELD_NUMBER: _ClassVar[int]
    PROP_OWNER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    INTERACT_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    GADGET_TALK_STATE_FIELD_NUMBER: _ClassVar[int]
    INIT_POSE_ID_FIELD_NUMBER: _ClassVar[int]
    PLAY_INFO_FIELD_NUMBER: _ClassVar[int]
    GATHER_GADGET_FIELD_NUMBER: _ClassVar[int]
    WORKTOP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_GADGET_FIELD_NUMBER: _ClassVar[int]
    WEATHER_FIELD_NUMBER: _ClassVar[int]
    ABILITY_GADGET_FIELD_NUMBER: _ClassVar[int]
    STATUE_GADGET_FIELD_NUMBER: _ClassVar[int]
    BOSS_CHEST_FIELD_NUMBER: _ClassVar[int]
    BLOSSOM_CHEST_FIELD_NUMBER: _ClassVar[int]
    MP_PLAY_REWARD_FIELD_NUMBER: _ClassVar[int]
    GENERAL_REWARD_FIELD_NUMBER: _ClassVar[int]
    OFFERING_INFO_FIELD_NUMBER: _ClassVar[int]
    FOUNDATION_INFO_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_INFO_FIELD_NUMBER: _ClassVar[int]
    SHELL_INFO_FIELD_NUMBER: _ClassVar[int]
    SCREEN_INFO_FIELD_NUMBER: _ClassVar[int]
    FISH_POOL_INFO_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_GADGET_TREE_INFO_FIELD_NUMBER: _ClassVar[int]
    ROGUELIKE_GADGET_INFO_FIELD_NUMBER: _ClassVar[int]
    NIGHT_CROW_GADGET_INFO_FIELD_NUMBER: _ClassVar[int]
    DESHRET_OBELISK_GADGET_INFO_FIELD_NUMBER: _ClassVar[int]
    COIN_COLLECT_OPERATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    TRIFLE_GADGET_FIELD_NUMBER: _ClassVar[int]
    gadget_id: int
    group_id: int
    config_id: int
    owner_entity_id: int
    born_type: _GadgetBornType_pb2.GadgetBornType
    gadget_state: int
    gadget_type: int
    is_show_cutscene: bool
    authority_peer_id: int
    is_enable_interact: bool
    interact_id: int
    mark_flag: int
    prop_owner_entity_id: int
    platform: _PlatformInfo_pb2.PlatformInfo
    interact_uid_list: _containers.RepeatedScalarFieldContainer[int]
    draft_id: int
    gadget_talk_state: int
    init_pose_id: int
    play_info: _GadgetPlayInfo_pb2.GadgetPlayInfo
    gather_gadget: _GatherGadgetInfo_pb2.GatherGadgetInfo
    worktop: _WorktopInfo_pb2.WorktopInfo
    client_gadget: _ClientGadgetInfo_pb2.ClientGadgetInfo
    weather: _WeatherInfo_pb2.WeatherInfo
    ability_gadget: _AbilityGadgetInfo_pb2.AbilityGadgetInfo
    statue_gadget: _StatueGadgetInfo_pb2.StatueGadgetInfo
    boss_chest: _BossChestInfo_pb2.BossChestInfo
    blossom_chest: _BlossomChestInfo_pb2.BlossomChestInfo
    mp_play_reward: _MpPlayRewardInfo_pb2.MpPlayRewardInfo
    general_reward: _GadgetGeneralRewardInfo_pb2.GadgetGeneralRewardInfo
    offering_info: _OfferingInfo_pb2.OfferingInfo
    foundation_info: _FoundationInfo_pb2.FoundationInfo
    vehicle_info: _VehicleInfo_pb2.VehicleInfo
    shell_info: _EchoShellInfo_pb2.EchoShellInfo
    screen_info: _ScreenInfo_pb2.ScreenInfo
    fish_pool_info: _FishPoolInfo_pb2.FishPoolInfo
    custom_gadget_tree_info: _CustomGadgetTreeInfo_pb2.CustomGadgetTreeInfo
    roguelike_gadget_info: _RoguelikeGadgetInfo_pb2.RoguelikeGadgetInfo
    night_crow_gadget_info: _NightCrowGadgetInfo_pb2.NightCrowGadgetInfo
    deshret_obelisk_gadget_info: _DeshretObeliskGadgetInfo_pb2.DeshretObeliskGadgetInfo
    coin_collect_operator_info: _CoinCollectOperatorInfo_pb2.CoinCollectOperatorInfo
    trifle_gadget: _TrifleGadget_pb2.TrifleGadget
    def __init__(self, gadget_id: _Optional[int] = ..., group_id: _Optional[int] = ..., config_id: _Optional[int] = ..., owner_entity_id: _Optional[int] = ..., born_type: _Optional[_Union[_GadgetBornType_pb2.GadgetBornType, str]] = ..., gadget_state: _Optional[int] = ..., gadget_type: _Optional[int] = ..., is_show_cutscene: bool = ..., authority_peer_id: _Optional[int] = ..., is_enable_interact: bool = ..., interact_id: _Optional[int] = ..., mark_flag: _Optional[int] = ..., prop_owner_entity_id: _Optional[int] = ..., platform: _Optional[_Union[_PlatformInfo_pb2.PlatformInfo, _Mapping]] = ..., interact_uid_list: _Optional[_Iterable[int]] = ..., draft_id: _Optional[int] = ..., gadget_talk_state: _Optional[int] = ..., init_pose_id: _Optional[int] = ..., play_info: _Optional[_Union[_GadgetPlayInfo_pb2.GadgetPlayInfo, _Mapping]] = ..., gather_gadget: _Optional[_Union[_GatherGadgetInfo_pb2.GatherGadgetInfo, _Mapping]] = ..., worktop: _Optional[_Union[_WorktopInfo_pb2.WorktopInfo, _Mapping]] = ..., client_gadget: _Optional[_Union[_ClientGadgetInfo_pb2.ClientGadgetInfo, _Mapping]] = ..., weather: _Optional[_Union[_WeatherInfo_pb2.WeatherInfo, _Mapping]] = ..., ability_gadget: _Optional[_Union[_AbilityGadgetInfo_pb2.AbilityGadgetInfo, _Mapping]] = ..., statue_gadget: _Optional[_Union[_StatueGadgetInfo_pb2.StatueGadgetInfo, _Mapping]] = ..., boss_chest: _Optional[_Union[_BossChestInfo_pb2.BossChestInfo, _Mapping]] = ..., blossom_chest: _Optional[_Union[_BlossomChestInfo_pb2.BlossomChestInfo, _Mapping]] = ..., mp_play_reward: _Optional[_Union[_MpPlayRewardInfo_pb2.MpPlayRewardInfo, _Mapping]] = ..., general_reward: _Optional[_Union[_GadgetGeneralRewardInfo_pb2.GadgetGeneralRewardInfo, _Mapping]] = ..., offering_info: _Optional[_Union[_OfferingInfo_pb2.OfferingInfo, _Mapping]] = ..., foundation_info: _Optional[_Union[_FoundationInfo_pb2.FoundationInfo, _Mapping]] = ..., vehicle_info: _Optional[_Union[_VehicleInfo_pb2.VehicleInfo, _Mapping]] = ..., shell_info: _Optional[_Union[_EchoShellInfo_pb2.EchoShellInfo, _Mapping]] = ..., screen_info: _Optional[_Union[_ScreenInfo_pb2.ScreenInfo, _Mapping]] = ..., fish_pool_info: _Optional[_Union[_FishPoolInfo_pb2.FishPoolInfo, _Mapping]] = ..., custom_gadget_tree_info: _Optional[_Union[_CustomGadgetTreeInfo_pb2.CustomGadgetTreeInfo, _Mapping]] = ..., roguelike_gadget_info: _Optional[_Union[_RoguelikeGadgetInfo_pb2.RoguelikeGadgetInfo, _Mapping]] = ..., night_crow_gadget_info: _Optional[_Union[_NightCrowGadgetInfo_pb2.NightCrowGadgetInfo, _Mapping]] = ..., deshret_obelisk_gadget_info: _Optional[_Union[_DeshretObeliskGadgetInfo_pb2.DeshretObeliskGadgetInfo, _Mapping]] = ..., coin_collect_operator_info: _Optional[_Union[_CoinCollectOperatorInfo_pb2.CoinCollectOperatorInfo, _Mapping]] = ..., trifle_gadget: _Optional[_Union[_TrifleGadget_pb2.TrifleGadget, _Mapping]] = ...) -> None: ...
