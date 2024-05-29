# Template `_example` dir

In the `templates` and `static/styles` folder there is an `_example` dir that is used to separate my testing templates from the lovely and well-styled documents in rest of the folder, by default it will serve yours, but to get my templates use the following commands

**MacOS / Linux**
```sh
TEMPLATE_PREFIX="_example" rye run dev
```

**Windows**
```sh
# Command Prompt
set TEMPLATE_PREFIX="_example"
rye run dev

# Powershell (the superiour windows shell)
$env:TEMPLATE_PREFIX="_example"
rye run dev
```

my pages (in the `_example` directory) are all different colours and are mostly un-styled so I can focus on writing pages that display stuff so you guys can look at them and help you write yours.

if the structure of your pages is different enough to warrant changing the [context](https://jinja.palletsprojects.com/en/3.0.x/templates/#variables) of what is passed to your pages, please feel free to message me as I want to make the process of writing this front-end as simple as possible so y'all can focus on making it look nice :D
