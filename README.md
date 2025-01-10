# Mad Libs Generator

This repository contains a Python program that generates a Mad Libs story by reading a template from a text file and replacing placeholders with user-provided words. It provides a fun and interactive way to create unique stories based on user input.

## Features
- Reads a story template from a `story.txt` file.
- Identifies placeholders in the format `<placeholder>` within the story.
- Prompts the user to input words for each placeholder.
- Replaces placeholders with the user-provided words to generate a complete story.
- Outputs the final story to the console.

## How It Works
1. The program reads the contents of `story.txt`.
2. It scans the text to find placeholders delimited by `<` and `>`.
3. The user is prompted to provide words for each unique placeholder.
4. The program replaces the placeholders with the user inputs and prints the final story.

## File Structure
```
madlibs_generator/
├── story.txt      # The story template file
├── madlibs.py     # The main Python script
└── README.md      # This readme file
```

## Prerequisites
- Python 3.x

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/madlibs_generator.git
   cd madlibs_generator
   ```

2. Create or modify the `story.txt` file with your story template. Use `<placeholder>` format for the words to be replaced.
   Example `story.txt`:
   ```
   Once upon a time in a <adjective> forest, there lived a <animal> who loved to <verb>.
   ```

3. Run the program:
   ```bash
   python madlibs.py
   ```

4. Enter words when prompted to fill in the placeholders and enjoy your unique story!

## Example Output
Given the `story.txt` template:
```
Once upon a time in a <adjective> forest, there lived a <animal> who loved to <verb>.
```

### Program Execution:
```bash
Enter a word for <adjective>: magical
Enter a word for <animal>: dragon
Enter a word for <verb>: fly
```

### Final Output:
```
Once upon a time in a magical forest, there lived a dragon who loved to fly.
```

## Customization
- Modify the `story.txt` file to create your own stories with different placeholders.

## Contributions
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy storytelling!
