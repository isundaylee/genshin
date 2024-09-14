from genshin.packet.proto import OneoffGatherPointDetectorData_pb2 as _OneoffGatherPointDetectorData_pb2
from genshin.packet.proto import ClientCollectorData_pb2 as _ClientCollectorData_pb2
from genshin.packet.proto import SkyCrystalDetectorQuickUseResult_pb2 as _SkyCrystalDetectorQuickUseResult_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuickUseWidgetRsp(_message.Message):
    __slots__ = ("retcode", "material_id", "detector_data", "client_collector_data", "sky_crystal_detector_quick_use_result")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_DATA_FIELD_NUMBER: _ClassVar[int]
    CLIENT_COLLECTOR_DATA_FIELD_NUMBER: _ClassVar[int]
    SKY_CRYSTAL_DETECTOR_QUICK_USE_RESULT_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    material_id: int
    detector_data: _OneoffGatherPointDetectorData_pb2.OneoffGatherPointDetectorData
    client_collector_data: _ClientCollectorData_pb2.ClientCollectorData
    sky_crystal_detector_quick_use_result: _SkyCrystalDetectorQuickUseResult_pb2.SkyCrystalDetectorQuickUseResult
    def __init__(self, retcode: _Optional[int] = ..., material_id: _Optional[int] = ..., detector_data: _Optional[_Union[_OneoffGatherPointDetectorData_pb2.OneoffGatherPointDetectorData, _Mapping]] = ..., client_collector_data: _Optional[_Union[_ClientCollectorData_pb2.ClientCollectorData, _Mapping]] = ..., sky_crystal_detector_quick_use_result: _Optional[_Union[_SkyCrystalDetectorQuickUseResult_pb2.SkyCrystalDetectorQuickUseResult, _Mapping]] = ...) -> None: ...
