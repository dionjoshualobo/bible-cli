# bible-cli

Clone, run the installer, and use the `bible` command.

Clone the repo:

```
git clone https://github.com/dionjoshualobo/bible-cli.git
cd bible-cli
```

Run the installer:

```
./install.sh
```

If the installer is not executable, make it so:

```
chmod +x ./install.sh
./install.sh
```

After installation run the `bible` command:

```
bible
```

Enjoy!

Windows
-------

On Windows you can run the PowerShell installer which copies files into your `%LOCALAPPDATA%` and adds a small `bible.cmd` wrapper to your user PATH.

Run in PowerShell from the repo directory:

```
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

You may need to open a new terminal after installation for the PATH change to take effect.
