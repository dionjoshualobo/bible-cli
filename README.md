# bible-cli

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
