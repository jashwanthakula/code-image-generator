import time
from flask import Flask, render_template, redirect, url_for, request
from threading import Thread
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import Python3Lexer
from utils import take_screenshot
from config import CODE

app = Flask(__name__)

@app.route("/")
def code():
    formatter = HtmlFormatter(style=app.config["CURRENT_THEME"])
    context = {
        "code": highlight(CODE, Python3Lexer(), formatter),
        "style_definitions": formatter.get_style_defs(),
        "style_bg_color": formatter.style.background_color
    }
    return render_template("base.html", **context)

@app.route("/make_image")
def make_image():
    target_url = request.host_url + url_for("code")
    take_screenshot(target_url)
    return redirect(url_for("code"))

def run_app():
    app.run(debug=False, use_reloader=False)

STYLES = ['abap', 'algol', 'algol_nu', 'arduino', 'autumn', 'bw', 'borland', 'coffee', 'colorful', 
          'default', 'dracula', 'emacs', 'friendly_grayscale', 'friendly', 'fruity', 'github-dark', 
          'gruvbox-dark', 'gruvbox-light', 'igor', 'inkpot', 'lightbulb', 'lilypond', 'lovelace', 
          'manni', 'material', 'monokai', 'murphy', 'native', 'nord-darker', 'nord', 'one-dark', 
          'paraiso-dark', 'paraiso-light', 'pastie', 'perldoc', 'rainbow_dash', 'rrt', 'sas', 
          'solarized-dark', 'solarized-light', 'staroffice', 'stata-dark', 'stata-light', 'tango', 
          'trac', 'vim', 'vs', 'xcode', 'zenburn']

if __name__ == "__main__":
    app_thread = Thread(target=run_app)
    app_thread.daemon = True
    app_thread.start()

    time.sleep(2)

    url = "http://127.0.0.1:5000/"
    for style in STYLES:
        print(f"Generating screenshot for style: {style}")
        app.config["CURRENT_THEME"] = style
        time.sleep(0.5)
        try:
            file_path = take_screenshot(url, filename=f"{style}_screenshot.png")
            print(f"Saved screenshot at: {file_path}")
        except Exception as e:
            print(f"Failed to generate screenshot for {style}: {str(e)}")
    
    print("All screenshots generated. Check the 'screenshots' folder.")