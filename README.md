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

 # bible-cli

A tiny command-line tool that prints random Bible verses from `bible.xml`.

## What it is

- **Purpose:** Prints a random Bible verse, or a verse from a specific book.
- **Platforms:** Linux, macOS, and Windows.
- **Primary files:** `bible` (CLI script), `bible.xml` (data), `books.py` (book metadata), `updater.py` (update/check logic).

## Tags & Options

- **`-b`, `--book` :** Specify a book to get a random verse from that book.
	- Usage:
		```bash
		bible -b BOOK
		bible --book BOOK
		bible --book=BOOK
		```
	- Examples:
		```bash
		bible -b Genesis
		bible -b Gen
		bible --book="1 Corinthians"
		```

- **`--list-books` :** Print a list of supported books and their abbreviations.

- **`-h`, `--help` :** Show help and usage information.

- **`--update` :** Download and install the latest release (or run `git pull` when inside a git checkout).

- **`--check-update` :** Dry-run check for updates. Exit codes:
	- `0` = up-to-date
	- `2` = update available
	- `1` = error / could not determine

## Linux / macOS — Setup, Run & Update

1. Clone the repo (optional — you can also download releases):

```bash
git clone https://github.com/dionjoshualobo/bible-cli.git
cd bible-cli
```

2. Install (from the repo root):

```bash
chmod +x ./install.sh
./install.sh
```

The installer copies the runtime files to `/usr/local/share/bible` and symlinks `/usr/local/bin/bible` so `bible` is available from your shell.

Note: The installer requires Python 3 on your PATH. Install it with your platform package manager if needed, e.g.:

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install python3

# macOS (Homebrew)
brew install python
```

3. Run the CLI:

```bash
bible            # print a random verse
bible --list-books
bible -b John
```

4. Update / Check for updates:

- If you installed from a git clone (developer copy):

```bash
cd /path/to/bible-cli
git pull origin main
```

- If you installed via the installer (non-git install), use the built-in updater:

```bash
bible --check-update   # dry-run: exit codes 0=up-to-date, 2=update available
bible --update         # download & run installer to update
```

## Windows — Setup, Run & Update

1. Clone or download the repo, then run the PowerShell installer from the repo directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

The Windows installer copies files into `%LOCALAPPDATA%\bible-cli` and creates a `bible.cmd` wrapper that launches the bundled Python invocation (tries `python`, then `py`).

2. Run the CLI in a new terminal:

```powershell
bible
bible --list-books
bible -b Genesis
```

3. Update / Check for updates on Windows:

- If you installed from a git clone, update with Git:

```powershell
cd C:\path\to\bible-cli
git pull origin main
```

- For installed copies use the built-in updater:

```powershell
bible --check-update
bible --update
```

## Contributing

Contributions are welcome. Please open an issue to discuss changes or submit a pull request with a clear description of the change. Keep changes focused and add tests/examples where appropriate.

- Report bugs: open an issue at https://github.com/dionjoshualobo/bible-cli/issues
- Submit PRs against `main` and include a brief description of why the change is needed.

Enjoy!
