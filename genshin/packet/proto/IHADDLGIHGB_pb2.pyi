from genshin.packet.proto import GLIEDEHAIMN_pb2 as _GLIEDEHAIMN_pb2
from genshin.packet.proto import KIDIOMKHFMO_pb2 as _KIDIOMKHFMO_pb2
from genshin.packet.proto import KEEHOCBAHKG_pb2 as _KEEHOCBAHKG_pb2
from genshin.packet.proto import MCLDAELJNIO_pb2 as _MCLDAELJNIO_pb2
from genshin.packet.proto import MMPHDJFAPGK_pb2 as _MMPHDJFAPGK_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IHADDLGIHGB(_message.Message):
    __slots__ = ("EHAEACFBOOL", "seek_furniture_gallery_info", "balloon_gallery_info", "stake_play_info", "explosion_info", "racing_gallery_info")
    EHAEACFBOOL_FIELD_NUMBER: _ClassVar[int]
    SEEK_FURNITURE_GALLERY_INFO_FIELD_NUMBER: _ClassVar[int]
    BALLOON_GALLERY_INFO_FIELD_NUMBER: _ClassVar[int]
    STAKE_PLAY_INFO_FIELD_NUMBER: _ClassVar[int]
    EXPLOSION_INFO_FIELD_NUMBER: _ClassVar[int]
    RACING_GALLERY_INFO_FIELD_NUMBER: _ClassVar[int]
    EHAEACFBOOL: int
    seek_furniture_gallery_info: _GLIEDEHAIMN_pb2.GLIEDEHAIMN
    balloon_gallery_info: _KIDIOMKHFMO_pb2.KIDIOMKHFMO
    stake_play_info: _KEEHOCBAHKG_pb2.KEEHOCBAHKG
    explosion_info: _MCLDAELJNIO_pb2.MCLDAELJNIO
    racing_gallery_info: _MMPHDJFAPGK_pb2.MMPHDJFAPGK
    def __init__(self, EHAEACFBOOL: _Optional[int] = ..., seek_furniture_gallery_info: _Optional[_Union[_GLIEDEHAIMN_pb2.GLIEDEHAIMN, _Mapping]] = ..., balloon_gallery_info: _Optional[_Union[_KIDIOMKHFMO_pb2.KIDIOMKHFMO, _Mapping]] = ..., stake_play_info: _Optional[_Union[_KEEHOCBAHKG_pb2.KEEHOCBAHKG, _Mapping]] = ..., explosion_info: _Optional[_Union[_MCLDAELJNIO_pb2.MCLDAELJNIO, _Mapping]] = ..., racing_gallery_info: _Optional[_Union[_MMPHDJFAPGK_pb2.MMPHDJFAPGK, _Mapping]] = ...) -> None: ...
