*This project has been created as part of the 42 curriculum by eberling.*

## Output preview (with --verbose)
<img width="940" height="230" alt="sortie" src="https://github.com/user-attachments/assets/33641c34-e6f0-4f59-9e54-294dbbd55c43" />

```
New state : State.READING_PROMPT_VALUE         <----- Each token is generated according to a part of the JSON format
Iteration 12/150
result value: {"prompt": "What is the square root of       <----      Here is the result showing while the LLM generating
Choosed token : '1' | Transition from state : {self.state_manager.state}      <------    We encourage more tokens corresponding to the characters we expect to have
New state : State.READING_PROMPT_VALUE
Iteration 13/150
result value: {"prompt": "What is the square root of 1
Choosed token : '6' | Transition from state : {self.state_manager.state}
New state : State.READING_PROMPT_VALUE
Iteration 14/150
result value: {"prompt": "What is the square root of 16
Choosed token : '?' | Transition from state : {self.state_manager.state}
New state : State.EXPECT_NAME_KEY
```


We encourage the tokens corresponding to json format like "{" in vocab below would be Token id *90* : etc...

Qwen/Qwen3-0.6B vocab file  ->  [Qwen/Qwen3-0.6B vocab](https://huggingface.co/Qwen/Qwen3-0.6B/raw/main/vocab.json)

## Description
This project, **Call Me Maybe**, implements a robust function-calling tool for Large Language Models (LLMs) using **constrained decoding**. In small language models (like the 0.6B parameter `Qwen/Qwen3-0.6B` model), generating structured outputs such as valid JSON schema is highly unreliable. This system guides the model token-by-token using a custom finite state machine, guaranteeing that the output is always 100% syntactically valid JSON matching the exact schema definition provided.

The system translates natural language requests (e.g., "What is the sum of 2 and 3?") into precise function calls with typed arguments (e.g., `{"name": "fn_add_numbers", "parameters": {"a": 2.0, "b": 3.0}}`).

## Instructions

### Installation
This project manages its dependencies using `uv`. Make sure you have `uv` installed, then run:
```bash
make install
```
This command will create a local virtual environment and install all required packages (including `numpy` and `pydantic` as specified by the subject).

### Execution
To run the main program using the default paths:
```bash
make run
```
You can also execute the script with custom paths using:
```bash
uv run python -m src --functions_definition <path_to_definitions> --input <path_to_inputs> --output <path_to_outputs>
```

### Formatting and Linting
To check the code for syntax, style (flake8), and type safety (mypy), run:
```bash
make lint
```

---

## Algorithm Explanation
The core of this project is **Constrained Decoding** powered by a Finite State Machine (FSM):
1. **FSM State Management (`JSONStateManager`)**: The FSM tracks the current token position in the expected JSON schema. It transitions through states such as:
   - `WAIT_FOR_OPEN_BRACE`
   - `EXPECT_PROMPT_KEY` / `READING_PROMPT_VALUE`
   - `EXPECT_NAME_KEY` / `READING_NAME_VALUE` (restricts choices to available function names)
   - `EXPECT_PARAMETERS_KEY`
   - `EXPECT_PARAM_KEY` / `READING_PARAM_VALUE` (enforces correct data types: strings, numbers, integers)
   - `EXPECT_CLOSE_BRACE`
2. **Logit Masking (`JSONLogitsProcessor`)**: At each token generation step, the `JSONLogitsProcessor` fetches the list of allowed strings/characters from the `JSONStateManager`. It encodes these candidates into token IDs, creates a mask for the vocabulary logits, setting all invalid token logits to `-inf`, and forces the model to sample only from the valid token subset.
3. **Loop Control (`ConstrainedDecoder`)**: Generates tokens iteratively, updating the generation context and feeding the generated token back to the FSM until the `State.DONE` or the EOS token is reached.

---

## Design Decisions
* **State Machine for Token Validation**: Instead of using regex or parsing partial JSON, a character-based FSM was chosen because it allows us to precisely know what token is expected next and build exact prefix lists for the tokenizer.
* **Separation of LLM and Processor**: The decoding loop is fully decoupled from the state validation logic, making the code testable and easy to modify.
* **Minimal Dependencies**: The project avoids forbidden external libraries (like `transformers` or `pytorch` in the client code) by strictly using the provided `llm_sdk` wrapper class.

---

## Example Usage

Run the program:
```bash
uv run python -m src \
  --functions_definition data/input/functions_definition.json \
  --input data/input/function_calling_tests.json \
  --output data/output/function_calling_results.json
```

**Input prompt (e.g. `function_calling_tests.json`)**:
```json
[
  {
    "prompt": "What is the sum of 2 and 3?"
  }
]
```

**Output result (`function_calling_results.json`)**:
```json
[
  {
    "prompt": "What is the sum of 2 and 3?",
    "name": "fn_add_numbers",
    "parameters": {
      "a": 2.0,
      "b": 3.0
    }
  }
]
```

---

## Resources
* Hugging Face Transformers documentation: [https://huggingface.co/docs/transformers](https://huggingface.co/docs/transformers)
* BPE and WordPiece Tokenization concepts.
* **AI Usage**: Gemini for designing, having a better understanding of the project's requirement, writing documentation, debugging 
