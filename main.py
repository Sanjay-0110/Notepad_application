from flet import (UserControl,
                  TextField,
                  InputBorder,
                  ControlEvent,
                  app)

from flet_core import Page


class TextEditor(UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.textfield = TextField(multiline=True,
                                   autofocus=True,
                                   border=InputBorder.NONE,
                                   min_lines=50,
                                   on_change=self.save_text,
                                   content_padding=30,
                                   cursor_color='yellow')

    def save_text(self, event=None) -> None:
        with open("save.txt", "w") as f:
            f.write(self.textfield.value)
            ''' textfield.value this going to grab anything inside the textfield at the time and save it txt file
            Now we need the method that loads the text when we restart the our code the text editor what value should
            be there.'''

    def read_text(self) -> str | None:
        try:
            with open("save.txt", "r") as f:
                return f.read()
        except FileNotFoundError:
            self.textfield.hint_text = " welcome to Notepad"

    # bulid method

    def build(self) -> TextField:
        self.textfield.value = self.read_text()
        return self.textfield


def main(page: Page) -> None:
    page.title = "Text Editor"
    page.scroll = True

    page.add(TextEditor())


if __name__ == "__main__":
    app(target=main)
