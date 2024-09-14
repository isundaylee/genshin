from genshin.packet.proto import Item_pb2 as _Item_pb2
from genshin.packet.proto import TrialAvatarGrantRecord_pb2 as _TrialAvatarGrantRecord_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrialAvatarInfo(_message.Message):
    __slots__ = ("trial_avatar_id", "trial_equip_list", "grant_record")
    TRIAL_AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_EQUIP_LIST_FIELD_NUMBER: _ClassVar[int]
    GRANT_RECORD_FIELD_NUMBER: _ClassVar[int]
    trial_avatar_id: int
    trial_equip_list: _containers.RepeatedCompositeFieldContainer[_Item_pb2.Item]
    grant_record: _TrialAvatarGrantRecord_pb2.TrialAvatarGrantRecord
    def __init__(self, trial_avatar_id: _Optional[int] = ..., trial_equip_list: _Optional[_Iterable[_Union[_Item_pb2.Item, _Mapping]]] = ..., grant_record: _Optional[_Union[_TrialAvatarGrantRecord_pb2.TrialAvatarGrantRecord, _Mapping]] = ...) -> None: ...
