from genshin.packet.proto import FurnitureMakeMakeInfo_pb2 as _FurnitureMakeMakeInfo_pb2
from genshin.packet.proto import FurnitureMakeHelpData_pb2 as _FurnitureMakeHelpData_pb2
from genshin.packet.proto import FurnitureMakeBeHelpedData_pb2 as _FurnitureMakeBeHelpedData_pb2
from genshin.packet.proto import FurnitureMakeSlot_pb2 as _FurnitureMakeSlot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FurnitureMakeRsp(_message.Message):
    __slots__ = ("make_info_list", "retcode", "help_data_list", "helped_data_list", "furniture_make_slot")
    MAKE_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    HELP_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    HELPED_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_MAKE_SLOT_FIELD_NUMBER: _ClassVar[int]
    make_info_list: _containers.RepeatedCompositeFieldContainer[_FurnitureMakeMakeInfo_pb2.FurnitureMakeMakeInfo]
    retcode: int
    help_data_list: _containers.RepeatedCompositeFieldContainer[_FurnitureMakeHelpData_pb2.FurnitureMakeHelpData]
    helped_data_list: _containers.RepeatedCompositeFieldContainer[_FurnitureMakeBeHelpedData_pb2.FurnitureMakeBeHelpedData]
    furniture_make_slot: _FurnitureMakeSlot_pb2.FurnitureMakeSlot
    def __init__(self, make_info_list: _Optional[_Iterable[_Union[_FurnitureMakeMakeInfo_pb2.FurnitureMakeMakeInfo, _Mapping]]] = ..., retcode: _Optional[int] = ..., help_data_list: _Optional[_Iterable[_Union[_FurnitureMakeHelpData_pb2.FurnitureMakeHelpData, _Mapping]]] = ..., helped_data_list: _Optional[_Iterable[_Union[_FurnitureMakeBeHelpedData_pb2.FurnitureMakeBeHelpedData, _Mapping]]] = ..., furniture_make_slot: _Optional[_Union[_FurnitureMakeSlot_pb2.FurnitureMakeSlot, _Mapping]] = ...) -> None: ...
