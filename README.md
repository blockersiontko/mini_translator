# Polish to English Mini Dictionary 📚

A simple Python program that translates Polish words into English words. Doesn't have that big of a dictionary, because it was mostly made as a learning project!

## Features

* Translates animal names from Polish to English.
* Validates user input.
* Repeats the prompt until a valid animal name is entered.
* Uses a Python dictionary for fast lookups.

## Words Included

| Polish       | English        |
| ------------ | -------------- |
| kot          | cat            |
| pies         | dog            |
| panda        | panda          |
| lis          | fox            |
| wilk         | wolf           |
| wąż          | snake          |
| niedźwiedź   | bear           |
| koń          | horse          |
| konik morski | seahorse       |
| ryba         | fish           |
| skrzypołcz   | horseshoe crab |

## Installation

Clone this repository:

```bash
git clone https://github.com/blockersiontko/mini_translator.git
```

Move into the project directory:

```bash
cd mini_translator
```

## How to Run

Run the Python script:

```bash
python interface.py
```

## Example

```text
PL: koń
EN: horse
```

If an invalid word is entered:

```text
PL: kiełbasa
EN: Nie znam takiego słowa!
```

## Repository

GitHub: https://github.com/blockersiontko/mini_translator

## Technologies Used

### GUI

* tkinter
* ttk
* grid

### LIBRARIES

* tkinter
* [requests](https://github.com/psf/requests) (Apache 2.0) - CaseInsensitiveDict

### LOGIC

* Case Insensitive Dictionary - (requests.structures.CaseInsensitiveDict)
* dictionary.py

## Future Improvements

* Make GUI cleaner
* Both side translation
* Copy results to clipboard
* API Connection
* Clear button
* Dark Theme

## Considered Features

* Live translating
* Synonyms support
* Suggestions when misspell
* Translation history
* Adding your own words from GUI level

## License

This project is licensed under the MIT License.