import json
from typing import Any, Dict, List


class FunctionSchema:
    def __init__(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            self.defined_functions: List[Dict[str, Any]] = json.load(f)

        self.functions_map = {f["name"]: f for f in self.defined_functions}

    def get_function(self, name: str) -> Dict[str, Any] | None:
        return self.functions_map.get(name)

    def get_all_names(self) -> List[str]:
        return list(self.functions_map.keys())
