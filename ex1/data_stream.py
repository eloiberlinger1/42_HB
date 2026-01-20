#!/usr/bin/env python3
"""
Docstring for ex1.data_stream
"""

from typing import Any, List, Optional, Union, Dict
from abc import ABC, abstractmethod


class DataStream(ABC):
    """
    Docstring for DataProcessor
    """
    def __init__(self, stream_id: str, type: str) -> None:
        self.stream_id = stream_id
        self.type = type
        pass

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        for d in data_batch:
            print(d)

        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    """
    Docstring for SensorStream
    """
    def __init__(self, stream_id: str) -> None:
        type = "Environmental Data"
        super().__init__(stream_id, type)

    def process_batch(self, data_batch: List[Any]) -> str:
        print("process batch of sensor stream")


class TransactionStream(DataStream):
    """
    Docstring for TransactionStream
    """
    def __init__(self, stream_id):
        type = "Financial Data"
        super().__init__(stream_id, type)


class EventStream(DataStream):
    """
    Docstring for EventStream
    """
    def __init__(self, stream_id):
        type = "System Events"
        super().__init__(stream_id, type)


class StreamProcessor():
    """
    Manages multiple DataStream based classes
    """
    def __init__(self, batch: any):
        """
        Docstring for __init__

        :param self: Description
        :param batch: Description
        :type batch: any
        """


def data_stream() -> None:
    """
    Docstring for data_stream
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("Initializing Sensor Stream...")
    sensor_001 = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_001.stream_id}, Type: {sensor_001.type}")

    dumy_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {dumy_data}")
    # sensor_001.process_batch(dumy_data)


if __name__ == "__main__":
    data_stream()
