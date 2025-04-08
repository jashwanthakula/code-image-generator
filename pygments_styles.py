from pygments.styles import get_all_styles

styles_list = list(get_all_styles())
print(styles_list)
print(len(styles_list))
for style in get_all_styles():
    print(style)