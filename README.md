<h1>BSE 202 - "Cross Platform Development"</h1>

- [Setting Up Rye](#setting-up-rye)
	- [Note: Windows Installer](#note-windows-installer)
	- [Uninstalling Rye](#uninstalling-rye)
- [Running](#running)
- [Linting and Formatting](#linting-and-formatting)

This project is primarily managed using [`rye`](https://rye-up.com).
If you know python virtual envrionments well, use them, I'm using `rye` because python venv's are horrible. 

## Setting Up Rye

Rye is a package management and venv management solution for python, it's Free, Open Source, MIT Licensed, and written by [Mitsuhiko](https://github.com/Mitsuhiko) (the original creator of flask). We will be using to provide a reproducable and stable development environment.

To download rye, head to [https://rye-up.com/](https://rye-up.com/) and scroll to the **Installation Instructions**, and select the download for 64-bit Windows (assuming you're on windows), if you're using Linux or MacOS, simply run `curl -sSf https://rye-up.com/get | bash`.

### Note: Windows Installer

Running this wil spawn a terminal window, it'll ask sometimes whether you would like to proceed or change something, leave the default as they are and if it asks a (y/n) question, please press `y + enter` to continue.

### Uninstalling Rye

Rye is able to completely uninstall itself, restoring your machine to a state from before it was there, simply run

```
rye self uninstall
```

And it should leave your system entirely.

## Running

First you'll need to sync the venv with `rye`

```
rye sync
```

You can then start a dev server with

```
rye run dev
```

## Linting and Formatting

Rye come built-in with a couple of utilities for keeping code well-formatted and compliant.

Running either of these commands will use [`ruff`](https://github.com/astral-sh/ruff) to format or [lint](https://en.wikipedia.org/wiki/Lint_(software)) your code respectively.

```
rye fmt
rye lint
```

---

Happy Coding :D