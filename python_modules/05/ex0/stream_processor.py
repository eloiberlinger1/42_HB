#!/usr/bin/env python3
"""
Docstring for ex0.stream_processor
"""

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    Docstring for DataProcessor
    """
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):
    """
    Docstring for NumericProcessor
    """

    def __init__(self) -> None:
        self.listelmt = None
        super().__init__()

    def process(self, data: Any) -> str:
        """
        Docstring for process

        First the data list has to be processed.
        """
        self.listelmt = data
        return str(data)

    def validate(self, data: Any) -> bool:
        """
        Docstring for validate

        Then it has to be validated
        """
        if (self.listelmt is None):
            return (False)
        try:
            parameter = str(data)
            self_data = str(self.listelmt)
            if (parameter != self_data):
                return (False)

            for i in self.listelmt:
                i = int(i)
            return (True)
        except Exception:
            return (False)

    def format_output(self, result: str) -> str:
        """
        Docstring for format_output
        """
        # If data has not been processed
        if (self.listelmt is None):
            return ("ERROR - Data not processed yet")
        try:
            liste = self.listelmt
            avg = sum(liste) / len(liste)
            return f"{len(liste)} numeric values, sum={sum(liste)}, avg={avg}"
        except Exception as e:
            return (f"failed to give output format : {e}")


class TextProcessor(DataProcessor):
    """
    Docstring for TextProcessor
    """
    def __init__(self) -> None:
        self.data = None
        super().__init__()

    def process(self, data: Any) -> str:
        self.data = str(data)
        return (self.data)

    def validate(self, data: Any) -> bool:
        if (self.data is None):
            return (False)
        try:
            str(data)
            return (True)
        except Exception:
            return (False)

    def format_output(self, result: str) -> str:
        wc = len(result.split(" "))
        return (f"Processed text: {len(result)} characters, {wc} words")


class LogProcessor(DataProcessor):
    """
    Docstring for LogProcessor
    """
    def __init__(self) -> None:
        self.data = None
        super().__init__()

    def process(self, data: Any) -> str:
        self.data = str(data)
        return (self.data)

    def validate(self, data: Any) -> bool:
        self.data = str(data)
        if (':' in self.data):
            return (True)
        else:
            return (False)

    def format_output(self, result: str) -> str:
        if (self.data is None):
            return ("Data must be validated first")
        elif ("Connection timeout" in self.data):
            return ("[ALERT] ERROR level detected: Connection timeout")
        elif ("System ready" in self.data):
            return ("[INFO] INFO level detected: System ready")
        return ("[ALERT] ERROR level detected " + result)


def stream_processor() -> None:
    """
    Docstring for stream_processor
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    print("Initializing Numeric Processor...")
    numeric_process = NumericProcessor()
    dumy_data = [1, 2, 3, 4, 5]
    result = numeric_process.process(dumy_data)
    print(f"Processing data: {result}")

    if (numeric_process.validate(result)):
        print("Validation: Numeric data verified")
        print(f"Output: {numeric_process.format_output(result)}")
    else:
        print("Validation: FAILED")

    print()
    print("Initializing Text Processor...")
    text_processor = TextProcessor()
    dumy_data = "Hello Nexus World"
    result = text_processor.process(dumy_data)
    print(f'Processing data: "{dumy_data}"')
    if (text_processor.validate(result)):
        print("Validation: Text data verified")
    print(f"Output: {text_processor.format_output(result)}")

    print()
    print("Initializing Log Processor...")
    log_processor = LogProcessor()
    dumy_data = '"ERROR: Connection timeout"'
    result = log_processor.process(dumy_data)
    print(f'Processing data: {dumy_data}')
    if (log_processor.validate(result)):
        print("Validation: Log entry verified")
    else:
        print("FAILED TO VERIFY LOG ENTRY")

    print(f"Output: {log_processor.format_output(result)}")

    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    numeric_process = NumericProcessor()
    result = numeric_process.process([1, 2, 3])
    if (numeric_process.validate(result)):
        print(f"Result 1: Processed {numeric_process.format_output(result)}")
    text_processor = TextProcessor()
    result = text_processor.process("abcdef hijkl")
    if (text_processor.validate(result)):
        print(f"Result 2: {text_processor.format_output(result)}")
    log_processor = LogProcessor()
    result = log_processor.process("[INFO] : System ready")
    if (log_processor.validate(result)):
        print(f"Result 3: {log_processor.format_output(result)}")
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
