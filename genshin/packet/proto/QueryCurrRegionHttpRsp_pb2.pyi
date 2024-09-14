from genshin.packet.proto import RegionInfo_pb2 as _RegionInfo_pb2
from genshin.packet.proto import ForceUpdateInfo_pb2 as _ForceUpdateInfo_pb2
from genshin.packet.proto import StopServerInfo_pb2 as _StopServerInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryCurrRegionHttpRsp(_message.Message):
    __slots__ = ("retcode", "msg", "region_info", "client_secret_key", "region_custom_config_encrypted", "client_region_custom_config_encrypted", "gate_ticket", "force_update", "stop_server")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    REGION_INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    REGION_CUSTOM_CONFIG_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    CLIENT_REGION_CUSTOM_CONFIG_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    GATE_TICKET_FIELD_NUMBER: _ClassVar[int]
    FORCE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    STOP_SERVER_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    msg: str
    region_info: _RegionInfo_pb2.RegionInfo
    client_secret_key: bytes
    region_custom_config_encrypted: bytes
    client_region_custom_config_encrypted: bytes
    gate_ticket: str
    force_update: _ForceUpdateInfo_pb2.ForceUpdateInfo
    stop_server: _StopServerInfo_pb2.StopServerInfo
    def __init__(self, retcode: _Optional[int] = ..., msg: _Optional[str] = ..., region_info: _Optional[_Union[_RegionInfo_pb2.RegionInfo, _Mapping]] = ..., client_secret_key: _Optional[bytes] = ..., region_custom_config_encrypted: _Optional[bytes] = ..., client_region_custom_config_encrypted: _Optional[bytes] = ..., gate_ticket: _Optional[str] = ..., force_update: _Optional[_Union[_ForceUpdateInfo_pb2.ForceUpdateInfo, _Mapping]] = ..., stop_server: _Optional[_Union[_StopServerInfo_pb2.StopServerInfo, _Mapping]] = ...) -> None: ...
