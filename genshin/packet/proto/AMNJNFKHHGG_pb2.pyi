from genshin.packet.proto import PDKLICCIOBO_pb2 as _PDKLICCIOBO_pb2
from genshin.packet.proto import KMFNKOEIKCD_pb2 as _KMFNKOEIKCD_pb2
from genshin.packet.proto import ABKHLJOMBBC_pb2 as _ABKHLJOMBBC_pb2
from genshin.packet.proto import HAOHMPKBFBJ_pb2 as _HAOHMPKBFBJ_pb2
from genshin.packet.proto import CEKJIGPMDIO_pb2 as _CEKJIGPMDIO_pb2
from genshin.packet.proto import DPMMBEONCNB_pb2 as _DPMMBEONCNB_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AMNJNFKHHGG(_message.Message):
    __slots__ = ("change_gadget_state", "active_monster_group", "deactive_gadget", "deactive_monster_wave_current_group", "active_monster_wave", "active_gadget", "HLKDDNGCKJN")
    CHANGE_GADGET_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_MONSTER_GROUP_FIELD_NUMBER: _ClassVar[int]
    DEACTIVE_GADGET_FIELD_NUMBER: _ClassVar[int]
    DEACTIVE_MONSTER_WAVE_CURRENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_MONSTER_WAVE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_GADGET_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    change_gadget_state: _PDKLICCIOBO_pb2.PDKLICCIOBO
    active_monster_group: _KMFNKOEIKCD_pb2.KMFNKOEIKCD
    deactive_gadget: _ABKHLJOMBBC_pb2.ABKHLJOMBBC
    deactive_monster_wave_current_group: _HAOHMPKBFBJ_pb2.HAOHMPKBFBJ
    active_monster_wave: _CEKJIGPMDIO_pb2.CEKJIGPMDIO
    active_gadget: _DPMMBEONCNB_pb2.DPMMBEONCNB
    HLKDDNGCKJN: int
    def __init__(self, change_gadget_state: _Optional[_Union[_PDKLICCIOBO_pb2.PDKLICCIOBO, _Mapping]] = ..., active_monster_group: _Optional[_Union[_KMFNKOEIKCD_pb2.KMFNKOEIKCD, _Mapping]] = ..., deactive_gadget: _Optional[_Union[_ABKHLJOMBBC_pb2.ABKHLJOMBBC, _Mapping]] = ..., deactive_monster_wave_current_group: _Optional[_Union[_HAOHMPKBFBJ_pb2.HAOHMPKBFBJ, _Mapping]] = ..., active_monster_wave: _Optional[_Union[_CEKJIGPMDIO_pb2.CEKJIGPMDIO, _Mapping]] = ..., active_gadget: _Optional[_Union[_DPMMBEONCNB_pb2.DPMMBEONCNB, _Mapping]] = ..., HLKDDNGCKJN: _Optional[int] = ...) -> None: ...
