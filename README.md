# gnome-extension-sync
Automate Installation and Settings for Gnome Extensions

## Requirements

* Gnome Shell 3.34 or greater ```gnome-shell --version```
* Python 3.5 or greater ```python --version```
* PIP installed ```pip --version```

## How to Install

After verifying you have Python 3 and pip module manager installed, use the following command to install.
```
pip install --user gnome-extension-sync
```

## How to Use

#### Install Extensions and Settings
```
gnome-extension-sync run
```

#### Create a configuration file
```
gnome-extension-sync generate
```

#### Upload configuration
```
gnome-extension-sync upload
```

#### Download Configuration file
```
gnome-extension-sync download
```

#### Download & Sync
Remotely pull down your configuration file and install extensions.
```
gnome-extension-sync downloadrun
```

## Questions

What if an extension is already installed and gnome-extension-sync run is attempted?
gnome-extension-sync will detect if the extension is installed and take no action.

Will gnome-extension-sync update existing extensions?
Nope.


