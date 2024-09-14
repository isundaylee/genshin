from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VehicleLocationInfo(_message.Message):
    __slots__ = ("uid_list", "MEGKADCAAAJ", "pos", "entity_id", "FIPKPJPKJBN", "owner_uid", "rot", "gadget_id")
    UID_LIST_FIELD_NUMBER: _ClassVar[int]
    MEGKADCAAAJ_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FIPKPJPKJBN_FIELD_NUMBER: _ClassVar[int]
    OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    uid_list: _containers.RepeatedScalarFieldContainer[int]
    MEGKADCAAAJ: float
    pos: _Vector_pb2.Vector
    entity_id: int
    FIPKPJPKJBN: float
    owner_uid: int
    rot: _Vector_pb2.Vector
    gadget_id: int
    def __init__(self, uid_list: _Optional[_Iterable[int]] = ..., MEGKADCAAAJ: _Optional[float] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., entity_id: _Optional[int] = ..., FIPKPJPKJBN: _Optional[float] = ..., owner_uid: _Optional[int] = ..., rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., gadget_id: _Optional[int] = ...) -> None: ...
