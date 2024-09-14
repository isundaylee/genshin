from genshin.packet.proto import EquipParam_pb2 as _EquipParam_pb2
from genshin.packet.proto import MaterialDeleteInfo_pb2 as _MaterialDeleteInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MailItem(_message.Message):
    __slots__ = ("equip_param", "delete_info")
    EQUIP_PARAM_FIELD_NUMBER: _ClassVar[int]
    DELETE_INFO_FIELD_NUMBER: _ClassVar[int]
    equip_param: _EquipParam_pb2.EquipParam
    delete_info: _MaterialDeleteInfo_pb2.MaterialDeleteInfo
    def __init__(self, equip_param: _Optional[_Union[_EquipParam_pb2.EquipParam, _Mapping]] = ..., delete_info: _Optional[_Union[_MaterialDeleteInfo_pb2.MaterialDeleteInfo, _Mapping]] = ...) -> None: ...
