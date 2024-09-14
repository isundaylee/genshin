from genshin.packet.proto import ResVersionConfig_pb2 as _ResVersionConfig_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegionInfo(_message.Message):
    __slots__ = ("gateserver_ip", "gateserver_port", "pay_callback_url", "area_type", "resource_url", "data_url", "feedback_url", "bulletin_url", "resource_url_bak", "data_url_bak", "client_data_version", "handbook_url", "client_silence_data_version", "client_data_md5", "client_silence_data_md5", "res_version_config", "secret_key", "official_community_url", "client_version_suffix", "client_silence_version_suffix", "use_gateserver_domain_name", "gateserver_domain_name", "user_center_url", "account_bind_url", "cdkey_url", "privacy_policy_url", "next_resource_url", "next_res_version_config", "game_biz", "gateserver_ipv6_ip")
    GATESERVER_IP_FIELD_NUMBER: _ClassVar[int]
    GATESERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    PAY_CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    AREA_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    DATA_URL_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_URL_FIELD_NUMBER: _ClassVar[int]
    BULLETIN_URL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URL_BAK_FIELD_NUMBER: _ClassVar[int]
    DATA_URL_BAK_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    HANDBOOK_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SILENCE_DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DATA_MD5_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SILENCE_DATA_MD5_FIELD_NUMBER: _ClassVar[int]
    RES_VERSION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    OFFICIAL_COMMUNITY_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SILENCE_VERSION_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    USE_GATESERVER_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    GATESERVER_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_CENTER_URL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_BIND_URL_FIELD_NUMBER: _ClassVar[int]
    CDKEY_URL_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    NEXT_RES_VERSION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GAME_BIZ_FIELD_NUMBER: _ClassVar[int]
    GATESERVER_IPV6_IP_FIELD_NUMBER: _ClassVar[int]
    gateserver_ip: str
    gateserver_port: int
    pay_callback_url: str
    area_type: str
    resource_url: str
    data_url: str
    feedback_url: str
    bulletin_url: str
    resource_url_bak: str
    data_url_bak: str
    client_data_version: int
    handbook_url: str
    client_silence_data_version: int
    client_data_md5: str
    client_silence_data_md5: str
    res_version_config: _ResVersionConfig_pb2.ResVersionConfig
    secret_key: bytes
    official_community_url: str
    client_version_suffix: str
    client_silence_version_suffix: str
    use_gateserver_domain_name: bool
    gateserver_domain_name: str
    user_center_url: str
    account_bind_url: str
    cdkey_url: str
    privacy_policy_url: str
    next_resource_url: str
    next_res_version_config: _ResVersionConfig_pb2.ResVersionConfig
    game_biz: str
    gateserver_ipv6_ip: str
    def __init__(self, gateserver_ip: _Optional[str] = ..., gateserver_port: _Optional[int] = ..., pay_callback_url: _Optional[str] = ..., area_type: _Optional[str] = ..., resource_url: _Optional[str] = ..., data_url: _Optional[str] = ..., feedback_url: _Optional[str] = ..., bulletin_url: _Optional[str] = ..., resource_url_bak: _Optional[str] = ..., data_url_bak: _Optional[str] = ..., client_data_version: _Optional[int] = ..., handbook_url: _Optional[str] = ..., client_silence_data_version: _Optional[int] = ..., client_data_md5: _Optional[str] = ..., client_silence_data_md5: _Optional[str] = ..., res_version_config: _Optional[_Union[_ResVersionConfig_pb2.ResVersionConfig, _Mapping]] = ..., secret_key: _Optional[bytes] = ..., official_community_url: _Optional[str] = ..., client_version_suffix: _Optional[str] = ..., client_silence_version_suffix: _Optional[str] = ..., use_gateserver_domain_name: bool = ..., gateserver_domain_name: _Optional[str] = ..., user_center_url: _Optional[str] = ..., account_bind_url: _Optional[str] = ..., cdkey_url: _Optional[str] = ..., privacy_policy_url: _Optional[str] = ..., next_resource_url: _Optional[str] = ..., next_res_version_config: _Optional[_Union[_ResVersionConfig_pb2.ResVersionConfig, _Mapping]] = ..., game_biz: _Optional[str] = ..., gateserver_ipv6_ip: _Optional[str] = ...) -> None: ...
