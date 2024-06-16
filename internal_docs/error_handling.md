# Error Handling for Functions

In order to allow you guys to handle error well, I've created a convention for errors that you will be given in the templates, it looks like this

```py
error = {
	"kind": "error kind",
	"code" : "error_code",
	"message": "error message"
}
```

This can be accessed in Jinja Templates like so

```jinja
{% if error is defined %}
	kind: {{ error["kind"] }}
	code: {{ error["code"] }}
	message: {{ error["message"] }}
{% endif %}
```

> [!NOTE]
> 
> `error.kind`
>
> The error kind will always be one of the following
> 
> - `"user"` 
> 	
> 	This means the user is the problem, and the user gave us bad data
> 
> - `"server"`
>
> 	This means I'm the problem, and this is a bug

> [!TIP]
>
> `error.code`
>
> the error code is a machine readable code that is unique to each error that is thrown, and can be used to find the source of that error.
>
> This should **NOT** be shown to the user.

> [!TIP]
>
> `error.message`
>
> The error message will be a nicely formatted string that can be shown to the user.