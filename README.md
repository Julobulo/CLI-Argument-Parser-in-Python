# Python Command-Line Argument Parser

This repository contains a Python script for parsing command-line arguments. The `parse_arguments` function processes the provided arguments according to the options specified in a dictionary. It supports both short and long options, and includes an automatically generated help menu.

## Features

- **Support for Short and Long Options:** Handles both `-o` and `--option` formats.
- **Help Menu Generation:** Displays a help menu with `--help`.
- **Error Handling:** Provides meaningful error messages for unknown or invalid options.
- **Flexible Argument Parsing:** Differentiates between options that take values and flags that don't.

## Usage

### Defining Options

Define your options in a dictionary where each key is the option's long name, and its value is a dictionary with keys for the short name, long name, and help description.

```python
options = {
    'verbose': {'short': 'v', 'long': 'verbose', 'help': 'Enable verbose mode'},
    'output': {'short': 'o', 'long': 'output', 'help': 'Specify output file'},
    'port': {'short': 'p', 'long': 'port', 'help': 'Specify port number'},
}
```

### Parsing Arguments

Pass the command-line arguments (`sys.argv[1:]`) and the options dictionary to `parse_arguments`.

```python
import sys
from parser import parse_arguments

if __name__ == "__main__":
    options = {
        'verbose': {'short': 'v', 'long': 'verbose', 'help': 'Enable verbose mode'},
        'output': {'short': 'o', 'long': 'output', 'help': 'Specify output file'},
        'port': {'short': 'p', 'long': 'port', 'help': 'Specify port number'},
    }
    args = sys.argv[1:]
    parsed_args = parse_arguments(args, options)
    print("Parsed arguments:", parsed_args)
```

### Example Command

```
python script.py -v --output=result.txt -p=8080
```

This command will enable verbose mode, set the output file to `result.txt`, and specify the port number as `8080`.

## Code Explanation

### `parse_arguments` Function

The `parse_arguments` function processes the command-line arguments according to the options provided.

- **Help Option:** If `--help` is encountered, the help menu is displayed and the program exits.
- **Long Options:** Options starting with `--` are considered long options. They can be in the format `--option=value` or `--option value`.
- **Short Options:** Options starting with `-` are considered short options. They must be defined in the options dictionary.

### `print_help` Function

The `print_help` function generates a help menu based on the provided options.

```python
def print_help(options):
    print("Usage:")
    print("python script.py [options]")
    print("Options:")
    print(f"  -h, --help: Display the help menu")
    for option_name, option_details in options.items():
        print(f"  -{option_details['short']}, --{option_details['long']}: {option_details['help']}")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions.

## Contact

For any questions or suggestions, please open an issue or contact me directly.