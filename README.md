# BSE 202 - "Cross Platform Development"

This project is primarily managed using [`rye`](https://rye-up.com), if for some reason you are unable to use `rye`, you must install the following dependencies with `pip` in order to run the program.

- `Flask>=3.0.2`
- `markupsafe>=2.1.5`

If you know python virtual envrionments well, use them, I'm using `rye` because python venv's are horrible. 

## Running

First you'll need to sync the venv with `rye`

```
rye sync
```

You can then start a dev server with

```
rye run dev
```