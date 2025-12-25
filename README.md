# bible-cli

Clone, run the installer, and use the `bible` command. This project supports Linux, macOS and Windows.

Clone the repo:

# bible-cli

A tiny CLI that prints random Bible verses from `bible.xml`.

Quick usage:

	- Run: `bible` (prints a random verse)
	- List books: `bible --list-books`
	- Get a verse from a book: `bible -b Genesis`

Updating:

	- Check for updates (dry-run): `bible --check-update`
	- Download & install latest: `bible --update`

Install (Linux/macOS):

	./install.sh

Install (Windows):

	powershell -ExecutionPolicy Bypass -File .\install.ps1

Clone, run the installer, and use the `bible` command. This project supports Linux, macOS and Windows.

Clone the repo:

```
git clone https://github.com/dionjoshualobo/bible-cli.git
cd bible-cli
```

Linux / macOS
--------------

Run the installer from the repository root:

```
chmod +x ./install.sh
./install.sh
```

The installer copies the `bible` script and `bible.xml` to `/usr/local/share/bible` and symlinks `/usr/local/bin/bible` so you can run `bible` from your shell.

Note: The installer checks for `python3` or `python` on your PATH. If Python 3 is not found it will warn you at the end of the install. Please install Python 3 and re-run the installer (e.g. `sudo apt install python3` on Debian/Ubuntu, `brew install python` on macOS).

Windows
-------

On Windows, run the PowerShell installer which copies files into `%LOCALAPPDATA%\bible-cli`, creates a `bible.cmd` wrapper and (optionally) adds the install folder to your user PATH.

Run in PowerShell from the repo directory:

```
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

The Windows installer will create a `bible.cmd` wrapper that first tries the `python` command and falls back to the `py` launcher. If Python 3 is not found it will print a warning and instructions to install Python.

After installation open a new terminal and run:

```
bible
```

Enjoy!

## Tags

### `-b` / `--book` - Specify a Book

Get a random verse from a specific book of the Bible.

**Usage:**
```
bible -b BOOK
bible --book BOOK
bible --book=BOOK
```

**Examples:**
```
bible -b Genesis
bible -b Gen
bible --book=Psalms
bible --book Ps
bible -b "1 Corinthians"
bible -b 1Cor
```

You can use either the full book name or the standard abbreviation. For a complete list of books and their abbreviations, run:

```
bible -h
```

### `-h` / `--help` - Show Help

Display help information including all available book names and their standard abbreviations.

**Usage:**
```
bible -h
bible --help
```

This will show:
- Usage examples
- Complete list of Old Testament books and abbreviations
- Complete list of New Testament books and abbreviations

**Note:** If you enter an incorrect book name, the CLI will suggest the closest matching book name if it can find one.
