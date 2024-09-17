from django.template.library import Library

register = Library()

@register.filter("is")
def file_type(file, extension: str):
    return file.name.endswith(extension)

@register.filter("format_url")
def get_code(url):
    return f"https://www.youtube.com/embed/{url.split("=")[-1]}"