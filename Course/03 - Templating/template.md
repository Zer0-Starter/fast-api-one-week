# Templating with *Jinja*

Templates help us to render response from our API to a web page

## Jinja

*Jinja* is a templating engine written in Python. It's designed to help the rendering process of API responses.This templating engine makes use of curly braket `{}` to distinguish its expressions and synthax from regular HTML, text and any other variable.

- variable block synthax: {{}}
- synthax for structures: {% %}
- comment sythax: {# #}

### Filter

Filter in Jinja is not like in Python synthax. We use pipe symbole `|` to add them.

#### Default filter
It's used to replace the output of the passed value if it turns out to be `None`
```jinja
{{ todo.item | default('This is a default todo item') }}
```

#### Escape Filter
It's used to render raw HTML output:
```jinja
{{ "<title>Todo Application</title>" | escape }}
```

#### Conversion filters
They are used to convert one data type to another
```jinja
{{ 3.142 | int }}
{{ 31 | float }}
```

#### Join filter
This filter helps to join elements in a list to a string as in Python
```jinja
{{ ['Packt', 'produces', 'great', 'books'] | join(' ') }}
{# Packt produces great books --> is the output #}
```

#### Length filter
This filter is used to return the length of the object passed
```jinja
Todo count: {{ todo | length }}
```

### If statements
```jinja
{% if todo | length < 5 %}
    You don't have much items on your todo list!
{% else %}
    You have a busy day it seems!
{% endif %}
```

### Loops
```jinja
{% for todo in todos %}
    <b> {{ todo.item }} </b>
{% endfor %}
```

### Macros
A macro in *Jinja* is a function that return an HTML string. His main use case is to avoid repetition of code
```jinja
{% macro input(name, value='', type='text', size-20) %}
    <div class="form">
        <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
    </div>
{% endmacro %}
```
This way, to quickly create an input in our form, the macro can be called:
```
{{ input('item') }}
```
And it will return the following:
```html
<div class="form">
    <input type="text" name="item" value="" size="20">
</div>
```