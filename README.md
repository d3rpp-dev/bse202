<h1>BSE 202 - "Cross Platform Development"</h1>

- [Setting Up Rye](#setting-up-rye)
	- [Note: Windows Installer](#note-windows-installer)
	- [Uninstalling Rye](#uninstalling-rye)
- [Running](#running)
- [Linting and Formatting](#linting-and-formatting)
- [Development](#development)

This project is primarily managed using [`rye`](https://rye-up.com).
If you know python virtual envrionments well, use them, I'm using `rye` because python venv's are horrible. 

## Setting Up Rye

Rye is a package management and venv management solution for python, it's Free, Open Source, MIT Licensed, and written by [Mitsuhiko](https://github.com/Mitsuhiko) (the original creator of flask). We will be using to provide a reproducable and stable development environment.

To download rye, head to [https://rye-up.com/](https://rye-up.com/) and scroll to the **Installation Instructions**, and select the download for 64-bit Windows (assuming you're on windows), if you're using Linux or MacOS, simply run `curl -sSf https://rye-up.com/get | bash`.

### Note: Windows Installer

Running this wil spawn a terminal window, it'll ask sometimes whether you would like to proceed or change something, leave the default as they are and if it asks a (y/n) question, please press `y + enter` to continue.

### Uninstalling Rye

Rye is able to completely uninstall itself, restoring your machine to a state from before it was there, simply run

```sh
rye self uninstall
```

And it should leave your system entirely.

## Running

First you'll need to sync the venv with `rye`

```sh
rye sync
```

Next we'll need to fill out the environment variables with data, to do this, make a copy of [`./.env.example`](./.env.example) and rename it to just `.env`, then fill out the values between the quotes, i.e.

```bash
# .env
SECRET_KEY="<Secret Key to sign Tokens>"
```

This will add the required variables that allow the program to function.

Next we need to initialise the database

```bash
rye run init_db
```

This will use the schema from [`schema.sql`](./src/bse202/schema.sql) and [`sample_data.sql`](./src/bse202/sample_data.sql) to create the SQLite Database.

You can then start a dev server with

```sh
rye run dev
```

## Linting and Formatting

Rye come built-in with a couple of utilities for keeping code well-formatted and compliant.

Running either of these commands will use [`ruff`](https://github.com/astral-sh/ruff) to format or [lint](https://en.wikipedia.org/wiki/Lint_(software)) your code respectively.

```sh
rye fmt
rye lint
```

---


## Development

This repository uses a standard of 1 endpoint = 1 file, this means that 2 people can work on completely different endpoints and the development will never collide with the file.

There are comments found throughout these files that should explain what is going on, for the purposes of making this code readable (or at least, as readable as this language can be), please make sure you comment your code well, at the at the module level using multi-line comments, e.g.

> [!NOTE]
> A module comment should appear before anythign else in the file, including imports.

```py
"""
This is a multi line module comment
"""

# ... rest of file
```

> [!NOTE]
> For every capital letter I see in:
> 
> - a file name
> - a variable name
> - a folder name
>
> I will kill a puppy

---

Happy Coding :D