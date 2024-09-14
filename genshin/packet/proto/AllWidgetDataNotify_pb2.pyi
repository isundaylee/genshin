from genshin.packet.proto import OneoffGatherPointDetectorData_pb2 as _OneoffGatherPointDetectorData_pb2
from genshin.packet.proto import ClientCollectorData_pb2 as _ClientCollectorData_pb2
from genshin.packet.proto import WidgetCoolDownData_pb2 as _WidgetCoolDownData_pb2
from genshin.packet.proto import AnchorPointData_pb2 as _AnchorPointData_pb2
from genshin.packet.proto import LunchBoxData_pb2 as _LunchBoxData_pb2
from genshin.packet.proto import SkyCrystalDetectorData_pb2 as _SkyCrystalDetectorData_pb2
from genshin.packet.proto import WidgetSlotData_pb2 as _WidgetSlotData_pb2
from genshin.packet.proto import WeatherWizardData_pb2 as _WeatherWizardData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AllWidgetDataNotify(_message.Message):
    __slots__ = ("anchor_point_list", "oneoff_gather_point_detector_data_list", "client_collector_data_list", "normal_cool_down_data_list", "group_cool_down_data_list", "slot_list", "lunch_box_data", "weather_wizard_data", "sky_crystal_detector_data", "background_active_widget_list")
    ANCHOR_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    ONEOFF_GATHER_POINT_DETECTOR_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_COLLECTOR_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    NORMAL_COOL_DOWN_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUP_COOL_DOWN_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    SLOT_LIST_FIELD_NUMBER: _ClassVar[int]
    LUNCH_BOX_DATA_FIELD_NUMBER: _ClassVar[int]
    WEATHER_WIZARD_DATA_FIELD_NUMBER: _ClassVar[int]
    SKY_CRYSTAL_DETECTOR_DATA_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_ACTIVE_WIDGET_LIST_FIELD_NUMBER: _ClassVar[int]
    anchor_point_list: _containers.RepeatedCompositeFieldContainer[_AnchorPointData_pb2.AnchorPointData]
    oneoff_gather_point_detector_data_list: _containers.RepeatedCompositeFieldContainer[_OneoffGatherPointDetectorData_pb2.OneoffGatherPointDetectorData]
    client_collector_data_list: _containers.RepeatedCompositeFieldContainer[_ClientCollectorData_pb2.ClientCollectorData]
    normal_cool_down_data_list: _containers.RepeatedCompositeFieldContainer[_WidgetCoolDownData_pb2.WidgetCoolDownData]
    group_cool_down_data_list: _containers.RepeatedCompositeFieldContainer[_WidgetCoolDownData_pb2.WidgetCoolDownData]
    slot_list: _containers.RepeatedCompositeFieldContainer[_WidgetSlotData_pb2.WidgetSlotData]
    lunch_box_data: _LunchBoxData_pb2.LunchBoxData
    weather_wizard_data: _WeatherWizardData_pb2.WeatherWizardData
    sky_crystal_detector_data: _SkyCrystalDetectorData_pb2.SkyCrystalDetectorData
    background_active_widget_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, anchor_point_list: _Optional[_Iterable[_Union[_AnchorPointData_pb2.AnchorPointData, _Mapping]]] = ..., oneoff_gather_point_detector_data_list: _Optional[_Iterable[_Union[_OneoffGatherPointDetectorData_pb2.OneoffGatherPointDetectorData, _Mapping]]] = ..., client_collector_data_list: _Optional[_Iterable[_Union[_ClientCollectorData_pb2.ClientCollectorData, _Mapping]]] = ..., normal_cool_down_data_list: _Optional[_Iterable[_Union[_WidgetCoolDownData_pb2.WidgetCoolDownData, _Mapping]]] = ..., group_cool_down_data_list: _Optional[_Iterable[_Union[_WidgetCoolDownData_pb2.WidgetCoolDownData, _Mapping]]] = ..., slot_list: _Optional[_Iterable[_Union[_WidgetSlotData_pb2.WidgetSlotData, _Mapping]]] = ..., lunch_box_data: _Optional[_Union[_LunchBoxData_pb2.LunchBoxData, _Mapping]] = ..., weather_wizard_data: _Optional[_Union[_WeatherWizardData_pb2.WeatherWizardData, _Mapping]] = ..., sky_crystal_detector_data: _Optional[_Union[_SkyCrystalDetectorData_pb2.SkyCrystalDetectorData, _Mapping]] = ..., background_active_widget_list: _Optional[_Iterable[int]] = ...) -> None: ...
