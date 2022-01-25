from rich.markdown import Markdown
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit import ANSI

from .cell import rich_print

md = Markdown(
    r"""```
--==================================================--
 _______ ___. ___________                  .__
 \      \\_ |_\__    ___/__________  _____ |__|__  ___.
 /   |   \| __ \|    |_/ __ \_  __ \/     \|  \  \/  /.
/    |    \ \_\ \    |\  ___/|  | \/  Y Y  \  |>    <..
\____|__  /___  /____| \___  >__|  |__|_|  /__/__/\_ \.
........\/....\/...........\/............\/.........\/.
--==================================================--
```
    There are two modes: edit mode, and command mode.
    - `e`: enter the edit mode, allowing to type into the cell.
    - `esc`: exit the edit mode and enter the command mode.

    In edit mode:
    - `ctrl-e`: run cell.
    - `ctrl-r`: run cell and select below in edit mode.
    - `ctrl-o`: open cell in external editor.
    - `ctrl-t`: open cell result in external editor.
    - `ctrl-f`: save tmp file from cell and execute it.
    - `ctrl-s`: save.

    In command mode:

    - `up` or `k`: select cell above.
    - `down` or `j`: select cell below.
    - `ctrl-f`: current cell to the top.
    - `ctrl-g`: go to last cell.
    - `gg`: go to first cell.
    - `ctrl-up`: move cell above.
    - `ctrl-down`: move cell below.
    - `right` : scroll output right
    - `left` : scroll output left
    - `c-j` : scroll output down
    - `c-k` : scroll output up
    - `ctrl-b` : reset output scroll shift
    - `a`: insert cell above.
    - `b`: insert cell below.
    - `x`: cut the cell.
    - `c`: copy the cell.
    - `ctrl-v`: paste cell above.
    - `v`: paste cell below.
    - `o`: set as code cell.
    - `r`: set as Markdown cell.
    - `l`: clear cell outputs.
    - `ctrl-l`: clear all cell outputs.
    - `f`: fold current cell input.
    - `/`: Search.
    - `n`: Repeat last search.
    - `N`: Search backwards.
    - `m`,`<any>`: Set mark <key>.
    - `'`,`<any>`: Go to mark <key>.
    - `ctrl-e` or `enter`: run cell.
    - `ctrl-f` : focus current cell.
    - `ctrl-r` or `alt-enter`: run cell and select below.
    - `ctrl-s`: save.
    - `ctrl-p`: run all cells.
    - `ctrl-q`: exit.
    - `ctrl-h`: show help.
"""
)


class Help:

    help_mode: bool
    help_text: str
    help_window: Window
    help_line: int

    def show_help(self):
        self.help_mode = True
        self.help_text = rich_print(md)
        self.help_window = Window(
            content=FormattedTextControl(text=ANSI(self.help_text))
        )
        self.app.layout = Layout(self.help_window)
        self.help_line = 0

    def scroll_help_up(self):
        if self.help_line > 0:
            self.help_line -= 1
            text = "\n".join(self.help_text.split("\n")[self.help_line :])  # noqa
            self.help_window.content = FormattedTextControl(text=ANSI(text))

    def scroll_help_down(self):
        if self.help_line < self.help_text.count("\n"):
            self.help_line += 1
            text = "\n".join(self.help_text.split("\n")[self.help_line :])  # noqa
            self.help_window.content = FormattedTextControl(text=ANSI(text))

    def quit_help(self):
        self.help_mode = False
        self.update_layout()
        self.help_text = rich_print(md, self.console)
        self.help_window = Window(
            content=FormattedTextControl(text=ANSI(self.help_text))
        )
