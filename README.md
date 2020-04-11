# gnome-extension-sync
Automate Installation and Settings for Gnome Extensions

## Purpose

The purpose is to automate your gnome's extensions. If you use multiple machines or distro hop, it's a pain to manually install extensions on each new installation. So, here is a single application to simply one part, installation and configuration of gnome extensions.

## Requirements

* Gnome Shell 3.36 or greater ```gnome-shell --version```
* Gnome Extensions ```gnome-extensions --version```
* Python 3.5 or greater ```python --version```
* PIP installed ```pip --version```

## How to Install

After verifying you have Python 3 and pip module manager installed, use the following command to install.
```
pip install --user gnome-extensions-sync
```

## Basic Use Cases and Examples

Step 1 - Generate a configuration file
```
gnome-extensions-sync generate
```


Now on a new machine, you just need to do 2 steps.
Step 1. Copy previously generated configuration file
Step 2. Run gnome-extension-sync

```
gnome-extensions-sync run
```

Step 3. Done



## Commands

#### Install Extensions and Settings
```
gnome-extensions-sync run
```

#### Create a configuration file
```
gnome-extensions-sync generate
```

#### Upload configuration
```
gnome-extensions-sync upload
```

#### Download Configuration file
```
gnome-extensions-sync download
```

#### Download & Sync
Remotely pull down your configuration file and install extensions.
```
gnome-extension-sync downloadrun
```

## Recommendations

Chezmoi is a command line tool to easily manage your dotfiles with git.
https://github.com/twpayne/chezmoi
https://fedoramagazine.org/take-back-your-dotfiles-with-chezmoi/

## Bug Reports

Create an issue, summary of the problem and include the following things
* Distro (`hostname`)
* Gnome Shell (`gnome-shell --version`)
* Gnome Extension version (`gnome-extensions`)
* gnome-extensions-sync configuration file (`~/.config/gnome-extensions-sync/extensions.json`)

## Questions

What if an extension is already installed and gnome-extension-sync run is attempted?
gnome-extension-sync will detect if the extension is installed and take no action.

Will gnome-extension-sync update existing extensions?
Nope.


