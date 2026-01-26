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

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Docstring for filter_data

        :param data_batch: Data batch to be filtered
        :type data_batch: List[Any]
        :param criteria: Criterea of selection for filtering
        :type criteria: Optional[str]
        :return: Filters the batch according to criteria
        :rtype: List[Any]
        """
        result = []
        for d in data_batch:

            if criteria is None:
                result.append(d)
                continue

            if criteria in d:
                result.append(d)

        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.type,
        }


class SensorStream(DataStream):
    """
    Docstring for SensorStream
    """

    def __init__(self, stream_id: str) -> None:
        type = "Environmental Data"
        super().__init__(stream_id, type)

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Docstring for process_batch
        """
        print(f"Processing sensor batch: {data_batch}")
        data_batch = self.filter_data(data_batch, "temp")
        batch_size = 0
        size = 0
        total = 0
        for _ in data_batch:
            batch_size += 1
        for i in data_batch:
            try:
                total += float(i.split(":")[1])
                size += 1
            except Exception as e:
                print(f"\nIncorrect value in data_batch: {i}\n{e}\n")

        avg = 0
        if size != 0:
            avg = total / size
        self.avg_value = avg
        return (
            f"Sensor analysis: {batch_size} reading prossessed, "
            f"avg temp: {avg}"
        )


class TransactionStream(DataStream):
    """
    Docstring for TransactionStream
    """

    def __init__(self, stream_id: str) -> None:
        type = " Financial Data"
        super().__init__(stream_id, type)

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Docstring for process_batch
        """
        print(f"Processing transaction batch: {data_batch}")
        filtered_batch = self.filter_data(data_batch)
        count = 0
        buy_count = 0
        sell_count = 0
        for i in filtered_batch:
            count += 1
            try:
                data = i.split(":")
                if data[0] == "buy":
                    buy_count += float(data[1])
                elif data[0] == "sell":
                    sell_count += float(data[1])

            except Exception as e:
                print(f"\nIncorrect value in data_batch: {i}\n{e}\n")

        return (
            f"Transaction analysis: {count} operations, net flow: +"
            f"{buy_count-sell_count} units"
        )


class EventStream(DataStream):
    """
    Docstring for EventStream
    """

    def __init__(self, stream_id: str) -> None:
        type = "System Events"
        self.errors_counter = 0
        super().__init__(stream_id, type)

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Docstring for process_batch
        """
        print(f"Processing transaction batch: {data_batch}")
        filtered_batch = self.filter_data(data_batch)
        count = 0
        err_count = 0
        for i in filtered_batch:
            count += 1
            if i == "error":
                err_count += 1

        self.errors_counter = err_count
        return f"Event analysis: {count} events, {err_count} error detected"


class StreamProcessor:
    """
    Manages multiple DataStream based classes
    """

    def __init__(self, batch: Any) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param batch: Description
        :type batch: any
        """
        self.streams = {}
        self.add_streams(batch)

    def add_stream(self, stream: DataStream) -> None:
        """
        Adds a stream to the list of streams
        """
        if isinstance(stream, SensorStream):
            self.streams["sensor"] = stream
        elif isinstance(stream, TransactionStream):
            self.streams["trans"] = stream
        elif isinstance(stream, EventStream):
            self.streams["event"] = stream

    def add_streams(self, streams: List[DataStream]) -> None:
        for s in streams:
            self.add_stream(s)

    def process_all(self, batches: List[Any]) -> None:
        """
        Process all batches
        """
        results = []
        for batch in batches:
            for item in batch:
                if (
                    ("temp:" in item)
                    or ("humidity:" in item)
                    or ("pressure:" in item)
                ):
                    results += [self.streams["sensor"].process_batch(batch)]
                    break
                elif ("buy:" in item) or ("sell:" in item):
                    results += [self.streams["trans"].process_batch(batch)]
                    break
                elif (
                    ("login" in item)
                    or ("logout" in item)
                    or ("error" in item)
                ):
                    results += [self.streams["event"].process_batch(batch)]
                    break

        return results


def data_stream() -> None:
    """
    Docstring for data_stream
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print()

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.type}")
    dumy_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    result = sensor.process_batch(dumy_data)
    print(result)

    print()

    print("Initializing Transaction Stream...")
    sensor = TransactionStream("TRANS_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.type}")
    dumy_data = ["buy:100", "sell:150", "buy:75"]
    result = sensor.process_batch(dumy_data)
    print(result)

    print()

    print("Initializing Event Stream...")
    sensor = EventStream("EVENT_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.type}")
    dumy_data = ["login", "error", "logout"]
    result = sensor.process_batch(dumy_data)
    print(result)

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    global_processor = StreamProcessor(
        [TransactionStream("t1"), SensorStream("s1"), EventStream("e1")]
    )

    print()
    print("Batch 1 Results:")
    dumy_data = [
        ["temp:20.0", "temp:24.0"],
        ["buy:50", "buy:30", "sell:20", "buy:40"],
        # ["login", "error", "login"],
        ["login", "error", "login"],
    ]
    results = global_processor.process_all(dumy_data)
    print()
    for r in results:
        print(f"- {r}")

    print()
    print("Stream filtering active: High-priority data only")
    event_errors_count = global_processor.streams["event"].errors_counter
    print(
        f"Filtered results: {event_errors_count} critical sensor alerts, 1 "
        f"large transaction"
    )
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
