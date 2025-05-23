# frl-tray
**frl-tray** is a simple Windows system tray utility that allows you to quickly view and set Nvidia's *Max Frame Rate* setting, also known as FRL (Frame Rate Limit). It's a GUI front-end for the [frl-toggle](https://github.com/FrogTheFrog/frl-toggle) CLI utility. This is intended to be useful in the case where you want quick manual access to this setting. Otherwise, you can use frl-toggle, or manage the FRL in the Nvidia App or Nvidia Control Panel.

## Features

- Easily see and select the current FRL
- Minimal tray interface
- Currently, the FRL is checked once when the app is started, and then only reflects changes made from the frl-tray utility

## Prerequisites

- Windows (tested on Windows 11 only)
- Nvidia GPU with support for the Max Frame Rate setting

## Quick Start

1. Download the latest (zip) release of `frl-tray`

2. Extract the folder to any desired install directory

3. Run `frl-tray.exe`

## Enable Auto-Start on Login (quick)

1. Create a shortcut for `frl-tray.exe` in `%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## Enable Auto-Start on Login (detailed)

1. Right click `frl-tray.exe` -> `Show More Options` -> `Create Shortcut`

2. Right click the `Start button` (Windows Logo) in the taskbar -> Run

3. In the `Run` dialog, type `shell:startup` and select `OK`

4. Move the shortcut you created into the Startup directory

## Building the exe

1. Install Python

2. Use pip to install pillow, pystray, and pyinstaller

3. Run `pyinstaller --onefile --noconsole frl-tray.py`
