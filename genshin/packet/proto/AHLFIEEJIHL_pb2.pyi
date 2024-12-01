from genshin.packet.proto import ABBFNMPEFPJ_pb2 as _ABBFNMPEFPJ_pb2
from genshin.packet.proto import HGJDNCCKHAE_pb2 as _HGJDNCCKHAE_pb2
from genshin.packet.proto import KHMODCLEFPE_pb2 as _KHMODCLEFPE_pb2
from genshin.packet.proto import OPGMGGFECMJ_pb2 as _OPGMGGFECMJ_pb2
from genshin.packet.proto import EMNDGKKCKGO_pb2 as _EMNDGKKCKGO_pb2
from genshin.packet.proto import ELBNIMPAMFP_pb2 as _ELBNIMPAMFP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AHLFIEEJIHL(_message.Message):
    __slots__ = ("ENOEKKLHBNH", "sync_create_connect", "sync_action", "sync_snap_shot", "sync_ping", "sync_finish_game", "EJNINFFFKJP")
    ENOEKKLHBNH_FIELD_NUMBER: _ClassVar[int]
    SYNC_CREATE_CONNECT_FIELD_NUMBER: _ClassVar[int]
    SYNC_ACTION_FIELD_NUMBER: _ClassVar[int]
    SYNC_SNAP_SHOT_FIELD_NUMBER: _ClassVar[int]
    SYNC_PING_FIELD_NUMBER: _ClassVar[int]
    SYNC_FINISH_GAME_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    ENOEKKLHBNH: _ABBFNMPEFPJ_pb2.ABBFNMPEFPJ
    sync_create_connect: _HGJDNCCKHAE_pb2.HGJDNCCKHAE
    sync_action: _KHMODCLEFPE_pb2.KHMODCLEFPE
    sync_snap_shot: _OPGMGGFECMJ_pb2.OPGMGGFECMJ
    sync_ping: _EMNDGKKCKGO_pb2.EMNDGKKCKGO
    sync_finish_game: _ELBNIMPAMFP_pb2.ELBNIMPAMFP
    EJNINFFFKJP: int
    def __init__(self, ENOEKKLHBNH: _Optional[_Union[_ABBFNMPEFPJ_pb2.ABBFNMPEFPJ, str]] = ..., sync_create_connect: _Optional[_Union[_HGJDNCCKHAE_pb2.HGJDNCCKHAE, _Mapping]] = ..., sync_action: _Optional[_Union[_KHMODCLEFPE_pb2.KHMODCLEFPE, _Mapping]] = ..., sync_snap_shot: _Optional[_Union[_OPGMGGFECMJ_pb2.OPGMGGFECMJ, _Mapping]] = ..., sync_ping: _Optional[_Union[_EMNDGKKCKGO_pb2.EMNDGKKCKGO, _Mapping]] = ..., sync_finish_game: _Optional[_Union[_ELBNIMPAMFP_pb2.ELBNIMPAMFP, _Mapping]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
