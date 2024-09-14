from genshin.packet.proto import TrialAvatarActivityRewardDetailInfo_pb2 as _TrialAvatarActivityRewardDetailInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrialAvatarActivityDetailInfo(_message.Message):
    __slots__ = ("reward_info_list",)
    REWARD_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    reward_info_list: _containers.RepeatedCompositeFieldContainer[_TrialAvatarActivityRewardDetailInfo_pb2.TrialAvatarActivityRewardDetailInfo]
    def __init__(self, reward_info_list: _Optional[_Iterable[_Union[_TrialAvatarActivityRewardDetailInfo_pb2.TrialAvatarActivityRewardDetailInfo, _Mapping]]] = ...) -> None: ...
