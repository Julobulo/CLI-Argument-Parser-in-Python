import sys

def parse_arguments(args, options):
    """
    Parse command-line arguments based on provided options.

    Args:
        args (list): List of command-line arguments.
        options (dict): Dictionary containing options and their details.
            Format: {'option_name': {'short': 's', 'long': 'long-name', 'help': 'Description of the option'}}

    Returns:
        dict: Parsed arguments as key-value pairs.
    """
    parsed_args = {}
    
    # Iterate through each argument provided in the command-line
    i = 0
    while i < len(args):
        arg = args[i]
        # If --help option is provided, print the help menu and exit
        if arg == '--help':
            print_help(options)
            sys.exit(0)
        # If the argument starts with --, it's a long option
        elif arg.startswith('--'):
            long_option = arg[2:]
            # Check if the value is provided after the option with an equal sign
            if '=' in long_option:
                option, value = long_option.split('=')
                if option not in options:
                    print(f"Unknown option:kkk {option}")
                    sys.exit(1)
                parsed_args[option] = value
            # Check if the long option is defined in the options dictionary
            elif long_option not in options:
                print(f"Unknown option: {arg}")
                sys.exit(1)
            else:
                # Check if the value is provided after the option
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    parsed_args[long_option] = args[i + 1]
                    i += 1
                else:
                    parsed_args[long_option] = True
        # If the argument starts with -, it's a short option
        elif arg.startswith('-'):
            # Iterate through each option and its details in the options dictionary
            for optionName, optionDescription in options.items():
                # If the short option matches the provided argument, set its value to True
                if arg[1:] == optionDescription['short']:
                    # Check if the value is provided after the option
                    if i + 1 < len(args) and not args[i + 1].startswith('-'):
                        parsed_args[optionDescription['long']] = args[i + 1]
                        i += 1
                    else:
                        parsed_args[optionDescription['long']] = True
                    break
            else:
                # If the provided option is not recognized, print an error message and exit
                print(f"Unknown option: {arg}")
                sys.exit(1)
        else:
            # If the argument is not an option (neither starting with -- nor -), print an error message and exit
            print(f"Invalid argument: {arg}")
            sys.exit(1)
        i += 1
    
    return parsed_args

def print_help(options):
    """
    Print help menu based on provided options.

    Args:
        options (dict): Dictionary containing options and their details.
    """
    print("Usage:")
    print("python script.py [options]")
    print("Options:")
    print(f"  -h, --help: Display the help menu")
    for option_name, option_details in options.items():
        # Print the short and long versions of the option along with its description
        print(f"  -{option_details['short']}, --{option_details['long']}: {option_details['help']}")

# Example usage
if __name__ == "__main__":
    # Define options with their short and long versions along with descriptions
    options = {
        'verbose': {'short': 'v', 'long': 'verbose', 'help': 'Enable verbose mode'},
        'output': {'short': 'o', 'long': 'output', 'help': 'Specify output file'},
        'port': {'short': 'p', 'long': 'port', 'help': 'Specify port number'},
    }
    # Get command-line arguments excluding the script name
    args = sys.argv[1:]
    # Parse the arguments based on the provided options
    parsed_args = parse_arguments(args, options)
    # Print the parsed arguments
    print("Parsed arguments:", parsed_args)
