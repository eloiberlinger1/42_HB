#!/usr/bin/env python3
"""
Docstring for ex2.nexus_pipeline
"""

from typing import Any, List, Union, Dict, Protocol
from abc import ABC, abstractmethod


# ################################################
#
#             STAGE - PROCESSINg CLASSES
#
# ################################################


# (Duck typing class)
class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any:
        pass


class InputStage:
    """
    Docstring for InputStage
    """

    def process(self, data: Any) -> Any:
        """
        Docstring for process

        This is the first of all the stages and can be called bt:
        - JSONAdapter (data format will be dict)
        - CSVAdapter (data format will be str (csv wise))
        - StreamAdapter (data format will be ??)
        """
        if data is None:
            raise ValueError("Data is corrupted")
        if not isinstance(data, (dict, list, str)):
            raise TypeError(f"Unsupported data type: {type(data)}")

        if isinstance(data, dict):
            if data["sensor"] is None:
                raise TypeError(f"Undefined values: {data}")

            if data["value"] is None:
                raise TypeError(f"Undefined values: {data}")

        if isinstance(data, dict):
            data["source_type"] = "JSON"

        elif isinstance(data, str):
            parts = data.split(",")
            if len(parts) >= 2:
                data = {"sensor": parts[0], "value": parts[1]}
            else:
                data = {"raw_content": data}
            data["source_type"] = "CSV"

        elif isinstance(data, list):
            data = {"data": data}
            data["source_type"] = "Stream"

        return data


class TransformStage:
    """
    Docstring for TransformStage
    """

    def process(self, data: Any) -> Any:
        """
        Processing the Transform stage
        adds nexus_verified as true if the data is successfully
        recognized as a dict.
        """
        if isinstance(data, dict):
            data["nexus_verified"] = True
        else:
            raise TypeError("Data must be dict")

        return data


class OutputStage:
    """
    Docstring for OutputStage
    """

    def process(self, data: Any) -> Any:
        if isinstance(data, dict):

            if data["source_type"] == "JSON":
                sensor = data.get("sensor", "unknown")
                val = data.get("value", "0")
                if data.get("nexus_verified"):
                    status = "Normal range"
                else:
                    status = "Unverified"

                return f"Processed {sensor} reading: {val}°C ({status})"

            elif data["source_type"] == "CSV":
                return "User activity logged: 1 actions processed"

            elif data["source_type"] == "Stream":
                length = len(data["data"])
                average = sum(data["data"]) / length
                return (
                    f"Output: Stream summary: {length}"
                    f" readings, avg: {average}°C"
                )

        else:
            raise TypeError("Input must be a dict")

        return data


class ProcessingPipeline(ABC):
    """
    Docstring for ProcessingPipeline
    """

    def __init__(self, pipeline_id: str) -> None:
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def _run_pipeline(self, data: Any) -> None:
        result = data
        for s in self.stages:
            result = s.process(result)
        return result

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


# ################################################
#
#             ADAPTERS CLASSES
#
# ################################################


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        """
        Docstring for __init__

        :param self: Description
        """
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """
        Docstring for process
        """
        print(f"Input: '{data}'")
        print(f"Processing JSON data through pipeline {self.pipeline_id}...")

        if not isinstance(data, dict):
            raise TypeError("JSONAdapter expect a dict")

        return self._run_pipeline(data)


class CSVAdapter(ProcessingPipeline):
    """
    Docstring for CSVAdapter
    """

    def __init__(self, pipeline_id: str) -> None:
        """
        Docstring for __init__

        :param self: Description
        """
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """
        Docstring for process
        """
        print(f"Input: '{data}'")
        print(f"Processing CSV data through pipeline {self.pipeline_id}...")

        if not isinstance(data, str):
            raise TypeError("CSVAdapter expect a string in CSV format")

        return self._run_pipeline(data)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        """
        Docstring for __init__

        :param self: Description
        """
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """
        Docstring for process
        """
        print(f"Input: '{data}'")
        print(f"Processing Stream data through pipeline {self.pipeline_id}...")

        if not isinstance(data, list):
            raise TypeError("StreamAdapter expect a list")

        return self._run_pipeline(data)


# ################################################
#
#             NEXUS CLASS
#
# ################################################


class NexusManager:
    """
    Docstring for NexusManager
    """

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.stats: Dict[str, Any] = {
            "total_processed": 0,
            "success_count": 0,
            "error_count": 0,
        }

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """
        To add a pipeline
        """

        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> None:
        for p in self.pipelines:
            try:
                result = p.process(data)
                self.stats["success_count"] += 1
                self.stats["total_processed"] += 1
                print(f"Result: {result}")
            except Exception as e:
                self.stats["error_count"] += 1
                print(f"Error detected: {e}")

    def chain_pipelines(
        self, data: Any, pipeline_list: List[ProcessingPipeline]
    ) -> Any:
        """
        Shows le chain system : Raw -> Processed -> Analyzed
        """
        current_data = data
        print("=== Pipeline Chaining Active ===")
        for p in pipeline_list:
            # previous result becomes the input of the next pipeline
            current_data = p.process(current_data)
        return current_data


# ################################################
#
#                  MAIN CODE
#
# ################################################


def nexus_pipeline() -> None:
    """
    Docstring for nexus_pipeline
    """
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    print()

    print("Initializing Nexus Manager...")
    print("")

    manager = NexusManager()

    # Configuration du pipeline JSON
    json_pipe = JSONAdapter("JSON_01")
    json_pipe.add_stage(InputStage())
    json_pipe.add_stage(TransformStage())
    json_pipe.add_stage(OutputStage())
    manager.add_pipeline(json_pipe)

    # Configuration du Pipeline CSV
    csv_pipe = CSVAdapter("CSV_LOG_01")
    csv_pipe.add_stage(InputStage())
    csv_pipe.add_stage(TransformStage())
    csv_pipe.add_stage(OutputStage())
    manager.add_pipeline(csv_pipe)

    # Configuration du Pipeline Stream
    stream_pipe = StreamAdapter("STREAM_01")
    stream_pipe.add_stage(InputStage())
    stream_pipe.add_stage(TransformStage())
    stream_pipe.add_stage(OutputStage())
    manager.add_pipeline(stream_pipe)

    test_data = {"sensor": "temp", "value": 23.5}
    manager.process_data(test_data)

    print("\n=== Multi-Format Data Processing ===")
    print()
    example_data = {"sensor": "temperature", "value": 23.5, "unit": "C"}
    manager.process_data(example_data)

    print()
    example_data = "user,action,timestamp"
    manager.process_data(example_data)

    print()
    print("Processing Stream data through same pipeline...")
    example_data = [20.0, 22.0, 24.0, 21.5, 23.0]
    manager.process_data(example_data)

    print()
    print("=== Pipeline Chaining Demo ===")
    print()

    chain_result = manager.chain_pipelines("user,login,12:00", [csv_pipe])
    print(f"Chaining result : {chain_result}")

    # test (les errures ne sont pas comptes ?!)
    print(f"\n\nManager stats: {manager.stats}")


if __name__ == "__main__":
    nexus_pipeline()
