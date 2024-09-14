from genshin.packet.proto import VehicleMember_pb2 as _VehicleMember_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VehicleInfo(_message.Message):
    __slots__ = ("member_list", "owner_uid", "cur_stamina", "GPMPAEGBEJE", "LLGKENMIENL", "anim_hash")
    MEMBER_LIST_FIELD_NUMBER: _ClassVar[int]
    OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    CUR_STAMINA_FIELD_NUMBER: _ClassVar[int]
    GPMPAEGBEJE_FIELD_NUMBER: _ClassVar[int]
    LLGKENMIENL_FIELD_NUMBER: _ClassVar[int]
    ANIM_HASH_FIELD_NUMBER: _ClassVar[int]
    member_list: _containers.RepeatedCompositeFieldContainer[_VehicleMember_pb2.VehicleMember]
    owner_uid: int
    cur_stamina: float
    GPMPAEGBEJE: int
    LLGKENMIENL: float
    anim_hash: int
    def __init__(self, member_list: _Optional[_Iterable[_Union[_VehicleMember_pb2.VehicleMember, _Mapping]]] = ..., owner_uid: _Optional[int] = ..., cur_stamina: _Optional[float] = ..., GPMPAEGBEJE: _Optional[int] = ..., LLGKENMIENL: _Optional[float] = ..., anim_hash: _Optional[int] = ...) -> None: ...
