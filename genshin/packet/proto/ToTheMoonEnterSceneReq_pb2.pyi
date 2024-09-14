from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ToTheMoonEnterSceneReq(_message.Message):
    __slots__ = ("DKEOBFMAFPK", "CDDPHGDDCCN", "scene_id", "version")
    DKEOBFMAFPK_FIELD_NUMBER: _ClassVar[int]
    CDDPHGDDCCN_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DKEOBFMAFPK: int
    CDDPHGDDCCN: int
    scene_id: int
    version: int
    def __init__(self, DKEOBFMAFPK: _Optional[int] = ..., CDDPHGDDCCN: _Optional[int] = ..., scene_id: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...
