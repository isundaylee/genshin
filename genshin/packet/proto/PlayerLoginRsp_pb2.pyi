from genshin.packet.proto import ShortAbilityHashPair_pb2 as _ShortAbilityHashPair_pb2
from genshin.packet.proto import ResVersionConfig_pb2 as _ResVersionConfig_pb2
from genshin.packet.proto import FeatureBlockInfo_pb2 as _FeatureBlockInfo_pb2
from genshin.packet.proto import StopServerInfo_pb2 as _StopServerInfo_pb2
from genshin.packet.proto import BlockInfo_pb2 as _BlockInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerLoginRsp(_message.Message):
    __slots__ = ("is_new_player", "game_biz", "OAMCACIICJJ", "player_data", "target_uid", "PCNBCFNBPGF", "ability_hash_code", "login_rand", "player_data_version", "client_silence_data_version", "retcode", "ability_hash_map", "client_data_version", "is_audit", "short_ability_hash_map", "res_version_config", "KLLPFNOLBHO", "KECGLOKOIDC", "feature_block_info_list", "EFPHHJIKPJG", "sc_info", "client_silence_version_suffix", "target_home_owner_uid", "JAGELBDJFJH", "msg", "CLJBEGINENC", "total_tick_time", "client_version_suffix", "ABPMACCDDJH", "next_resource_url", "PKEKLEEOLJL", "block_info_map", "birthday", "JKANELMFGEP", "is_data_need_relogin", "country_code", "next_res_version_config")
    class AbilityHashMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class BlockInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _BlockInfo_pb2.BlockInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_BlockInfo_pb2.BlockInfo, _Mapping]] = ...) -> None: ...
    IS_NEW_PLAYER_FIELD_NUMBER: _ClassVar[int]
    GAME_BIZ_FIELD_NUMBER: _ClassVar[int]
    OAMCACIICJJ_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DATA_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    PCNBCFNBPGF_FIELD_NUMBER: _ClassVar[int]
    ABILITY_HASH_CODE_FIELD_NUMBER: _ClassVar[int]
    LOGIN_RAND_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SILENCE_DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    ABILITY_HASH_MAP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_AUDIT_FIELD_NUMBER: _ClassVar[int]
    SHORT_ABILITY_HASH_MAP_FIELD_NUMBER: _ClassVar[int]
    RES_VERSION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    KLLPFNOLBHO_FIELD_NUMBER: _ClassVar[int]
    KECGLOKOIDC_FIELD_NUMBER: _ClassVar[int]
    FEATURE_BLOCK_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    EFPHHJIKPJG_FIELD_NUMBER: _ClassVar[int]
    SC_INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SILENCE_VERSION_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TARGET_HOME_OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    JAGELBDJFJH_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    CLJBEGINENC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TICK_TIME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    ABPMACCDDJH_FIELD_NUMBER: _ClassVar[int]
    NEXT_RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    PKEKLEEOLJL_FIELD_NUMBER: _ClassVar[int]
    BLOCK_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    JKANELMFGEP_FIELD_NUMBER: _ClassVar[int]
    IS_DATA_NEED_RELOGIN_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    NEXT_RES_VERSION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    is_new_player: bool
    game_biz: str
    OAMCACIICJJ: bool
    player_data: bytes
    target_uid: int
    PCNBCFNBPGF: bool
    ability_hash_code: int
    login_rand: int
    player_data_version: int
    client_silence_data_version: int
    retcode: int
    ability_hash_map: _containers.ScalarMap[str, int]
    client_data_version: int
    is_audit: bool
    short_ability_hash_map: _containers.RepeatedCompositeFieldContainer[_ShortAbilityHashPair_pb2.ShortAbilityHashPair]
    res_version_config: _ResVersionConfig_pb2.ResVersionConfig
    KLLPFNOLBHO: bool
    KECGLOKOIDC: str
    feature_block_info_list: _containers.RepeatedCompositeFieldContainer[_FeatureBlockInfo_pb2.FeatureBlockInfo]
    EFPHHJIKPJG: bool
    sc_info: bytes
    client_silence_version_suffix: str
    target_home_owner_uid: int
    JAGELBDJFJH: bool
    msg: str
    CLJBEGINENC: bool
    total_tick_time: float
    client_version_suffix: str
    ABPMACCDDJH: _StopServerInfo_pb2.StopServerInfo
    next_resource_url: str
    PKEKLEEOLJL: str
    block_info_map: _containers.MessageMap[int, _BlockInfo_pb2.BlockInfo]
    birthday: str
    JKANELMFGEP: str
    is_data_need_relogin: bool
    country_code: str
    next_res_version_config: _ResVersionConfig_pb2.ResVersionConfig
    def __init__(self, is_new_player: bool = ..., game_biz: _Optional[str] = ..., OAMCACIICJJ: bool = ..., player_data: _Optional[bytes] = ..., target_uid: _Optional[int] = ..., PCNBCFNBPGF: bool = ..., ability_hash_code: _Optional[int] = ..., login_rand: _Optional[int] = ..., player_data_version: _Optional[int] = ..., client_silence_data_version: _Optional[int] = ..., retcode: _Optional[int] = ..., ability_hash_map: _Optional[_Mapping[str, int]] = ..., client_data_version: _Optional[int] = ..., is_audit: bool = ..., short_ability_hash_map: _Optional[_Iterable[_Union[_ShortAbilityHashPair_pb2.ShortAbilityHashPair, _Mapping]]] = ..., res_version_config: _Optional[_Union[_ResVersionConfig_pb2.ResVersionConfig, _Mapping]] = ..., KLLPFNOLBHO: bool = ..., KECGLOKOIDC: _Optional[str] = ..., feature_block_info_list: _Optional[_Iterable[_Union[_FeatureBlockInfo_pb2.FeatureBlockInfo, _Mapping]]] = ..., EFPHHJIKPJG: bool = ..., sc_info: _Optional[bytes] = ..., client_silence_version_suffix: _Optional[str] = ..., target_home_owner_uid: _Optional[int] = ..., JAGELBDJFJH: bool = ..., msg: _Optional[str] = ..., CLJBEGINENC: bool = ..., total_tick_time: _Optional[float] = ..., client_version_suffix: _Optional[str] = ..., ABPMACCDDJH: _Optional[_Union[_StopServerInfo_pb2.StopServerInfo, _Mapping]] = ..., next_resource_url: _Optional[str] = ..., PKEKLEEOLJL: _Optional[str] = ..., block_info_map: _Optional[_Mapping[int, _BlockInfo_pb2.BlockInfo]] = ..., birthday: _Optional[str] = ..., JKANELMFGEP: _Optional[str] = ..., is_data_need_relogin: bool = ..., country_code: _Optional[str] = ..., next_res_version_config: _Optional[_Union[_ResVersionConfig_pb2.ResVersionConfig, _Mapping]] = ...) -> None: ...
