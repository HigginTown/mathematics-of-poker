# custom style
from IPython.core.display import HTML
def css_styling():
    styles = open("../../_style/custom.css", "r").read()
    return HTML(styles)
