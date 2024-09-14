from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import CreateGadgetInfo_pb2 as _CreateGadgetInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEntityInfo(_message.Message):
    __slots__ = ("level", "pos", "rot", "scene_id", "room_id", "client_unique_id", "monster_id", "npc_id", "gadget_id", "item_id", "gadget")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NPC_ID_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    GADGET_FIELD_NUMBER: _ClassVar[int]
    level: int
    pos: _Vector_pb2.Vector
    rot: _Vector_pb2.Vector
    scene_id: int
    room_id: int
    client_unique_id: int
    monster_id: int
    npc_id: int
    gadget_id: int
    item_id: int
    gadget: _CreateGadgetInfo_pb2.CreateGadgetInfo
    def __init__(self, level: _Optional[int] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., scene_id: _Optional[int] = ..., room_id: _Optional[int] = ..., client_unique_id: _Optional[int] = ..., monster_id: _Optional[int] = ..., npc_id: _Optional[int] = ..., gadget_id: _Optional[int] = ..., item_id: _Optional[int] = ..., gadget: _Optional[_Union[_CreateGadgetInfo_pb2.CreateGadgetInfo, _Mapping]] = ...) -> None: ...
