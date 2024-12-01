from genshin.packet.proto import EFPCNOOEDLC_pb2 as _EFPCNOOEDLC_pb2
from genshin.packet.proto import HJMPMBGECAE_pb2 as _HJMPMBGECAE_pb2
from genshin.packet.proto import NCCNCMFILPA_pb2 as _NCCNCMFILPA_pb2
from genshin.packet.proto import EKIAMHKEMOO_pb2 as _EKIAMHKEMOO_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LDFOEHIKKML(_message.Message):
    __slots__ = ("monster_group_deactive", "monster_wave_deactive", "gadget_state_change", "gadget_deactive", "HLKDDNGCKJN")
    MONSTER_GROUP_DEACTIVE_FIELD_NUMBER: _ClassVar[int]
    MONSTER_WAVE_DEACTIVE_FIELD_NUMBER: _ClassVar[int]
    GADGET_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    GADGET_DEACTIVE_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    monster_group_deactive: _EFPCNOOEDLC_pb2.EFPCNOOEDLC
    monster_wave_deactive: _HJMPMBGECAE_pb2.HJMPMBGECAE
    gadget_state_change: _NCCNCMFILPA_pb2.NCCNCMFILPA
    gadget_deactive: _EKIAMHKEMOO_pb2.EKIAMHKEMOO
    HLKDDNGCKJN: int
    def __init__(self, monster_group_deactive: _Optional[_Union[_EFPCNOOEDLC_pb2.EFPCNOOEDLC, _Mapping]] = ..., monster_wave_deactive: _Optional[_Union[_HJMPMBGECAE_pb2.HJMPMBGECAE, _Mapping]] = ..., gadget_state_change: _Optional[_Union[_NCCNCMFILPA_pb2.NCCNCMFILPA, _Mapping]] = ..., gadget_deactive: _Optional[_Union[_EKIAMHKEMOO_pb2.EKIAMHKEMOO, _Mapping]] = ..., HLKDDNGCKJN: _Optional[int] = ...) -> None: ...
