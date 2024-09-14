from genshin.packet.proto import SkyCrystalDetectorData_pb2 as _SkyCrystalDetectorData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkyCrystalDetectorQuickUseResult(_message.Message):
    __slots__ = ("sky_crystal_detector_data", "retcode")
    SKY_CRYSTAL_DETECTOR_DATA_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    sky_crystal_detector_data: _SkyCrystalDetectorData_pb2.SkyCrystalDetectorData
    retcode: int
    def __init__(self, sky_crystal_detector_data: _Optional[_Union[_SkyCrystalDetectorData_pb2.SkyCrystalDetectorData, _Mapping]] = ..., retcode: _Optional[int] = ...) -> None: ...
