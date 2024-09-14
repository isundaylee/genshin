from genshin.packet.proto import StopServerInfo_pb2 as _StopServerInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPlayerTokenRsp(_message.Message):
    __slots__ = ("retcode", "secret_key_seed", "is_guest", "security_cmd_buffer", "is_proficient_player", "account_uid", "black_uid_end_time", "uid", "extra_bin_data", "gm_uid", "secret_key", "account_type", "platform_type", "msg", "token", "server_rand_key", "AKODFAIGJCE", "MPGMOFLCEOF", "channel_id", "key_id", "GCDGEKAONGD", "KNCFLPGOMNI", "OLODGDMMPNF", "stop_server", "HNBGEKMPFIB", "JDHCKKAGBNL", "KEKHAKAPMIN", "CIJPMGMCJBA", "tag", "PLNNJPFPPAM", "country_code", "game_biz", "finish_collection_id_list", "birthday", "CEMENPADOPP", "sign", "psn_id", "JLCDDOJGKKG")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_SEED_FIELD_NUMBER: _ClassVar[int]
    IS_GUEST_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CMD_BUFFER_FIELD_NUMBER: _ClassVar[int]
    IS_PROFICIENT_PLAYER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_UID_FIELD_NUMBER: _ClassVar[int]
    BLACK_UID_END_TIME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_BIN_DATA_FIELD_NUMBER: _ClassVar[int]
    GM_UID_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SERVER_RAND_KEY_FIELD_NUMBER: _ClassVar[int]
    AKODFAIGJCE_FIELD_NUMBER: _ClassVar[int]
    MPGMOFLCEOF_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    GCDGEKAONGD_FIELD_NUMBER: _ClassVar[int]
    KNCFLPGOMNI_FIELD_NUMBER: _ClassVar[int]
    OLODGDMMPNF_FIELD_NUMBER: _ClassVar[int]
    STOP_SERVER_FIELD_NUMBER: _ClassVar[int]
    HNBGEKMPFIB_FIELD_NUMBER: _ClassVar[int]
    JDHCKKAGBNL_FIELD_NUMBER: _ClassVar[int]
    KEKHAKAPMIN_FIELD_NUMBER: _ClassVar[int]
    CIJPMGMCJBA_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    PLNNJPFPPAM_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    GAME_BIZ_FIELD_NUMBER: _ClassVar[int]
    FINISH_COLLECTION_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    CEMENPADOPP_FIELD_NUMBER: _ClassVar[int]
    SIGN_FIELD_NUMBER: _ClassVar[int]
    PSN_ID_FIELD_NUMBER: _ClassVar[int]
    JLCDDOJGKKG_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    secret_key_seed: int
    is_guest: bool
    security_cmd_buffer: bytes
    is_proficient_player: bool
    account_uid: str
    black_uid_end_time: int
    uid: int
    extra_bin_data: bytes
    gm_uid: int
    secret_key: str
    account_type: int
    platform_type: int
    msg: str
    token: str
    server_rand_key: str
    AKODFAIGJCE: bool
    MPGMOFLCEOF: int
    channel_id: int
    key_id: int
    GCDGEKAONGD: bool
    KNCFLPGOMNI: str
    OLODGDMMPNF: str
    stop_server: _StopServerInfo_pb2.StopServerInfo
    HNBGEKMPFIB: bool
    JDHCKKAGBNL: int
    KEKHAKAPMIN: int
    CIJPMGMCJBA: int
    tag: int
    PLNNJPFPPAM: int
    country_code: str
    game_biz: str
    finish_collection_id_list: _containers.RepeatedScalarFieldContainer[int]
    birthday: str
    CEMENPADOPP: str
    sign: str
    psn_id: str
    JLCDDOJGKKG: str
    def __init__(self, retcode: _Optional[int] = ..., secret_key_seed: _Optional[int] = ..., is_guest: bool = ..., security_cmd_buffer: _Optional[bytes] = ..., is_proficient_player: bool = ..., account_uid: _Optional[str] = ..., black_uid_end_time: _Optional[int] = ..., uid: _Optional[int] = ..., extra_bin_data: _Optional[bytes] = ..., gm_uid: _Optional[int] = ..., secret_key: _Optional[str] = ..., account_type: _Optional[int] = ..., platform_type: _Optional[int] = ..., msg: _Optional[str] = ..., token: _Optional[str] = ..., server_rand_key: _Optional[str] = ..., AKODFAIGJCE: bool = ..., MPGMOFLCEOF: _Optional[int] = ..., channel_id: _Optional[int] = ..., key_id: _Optional[int] = ..., GCDGEKAONGD: bool = ..., KNCFLPGOMNI: _Optional[str] = ..., OLODGDMMPNF: _Optional[str] = ..., stop_server: _Optional[_Union[_StopServerInfo_pb2.StopServerInfo, _Mapping]] = ..., HNBGEKMPFIB: bool = ..., JDHCKKAGBNL: _Optional[int] = ..., KEKHAKAPMIN: _Optional[int] = ..., CIJPMGMCJBA: _Optional[int] = ..., tag: _Optional[int] = ..., PLNNJPFPPAM: _Optional[int] = ..., country_code: _Optional[str] = ..., game_biz: _Optional[str] = ..., finish_collection_id_list: _Optional[_Iterable[int]] = ..., birthday: _Optional[str] = ..., CEMENPADOPP: _Optional[str] = ..., sign: _Optional[str] = ..., psn_id: _Optional[str] = ..., JLCDDOJGKKG: _Optional[str] = ...) -> None: ...
