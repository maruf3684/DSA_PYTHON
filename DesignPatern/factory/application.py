from abc import ABC,abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class TextBox(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        print("Rendering Windows-style Button")

class MacButton(Button):
    def render(self):
        print("Rendering Mac-style Button")


class WindowsTextBox(TextBox):
    def render(self):
        print("Rendering Windows-style TextBox")

class MacTextBox(TextBox):
    def render(self):
        print("Rendering Mac-style TextBox")

#######################################################


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        pass

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    def create_textbox(self) -> TextBox:
        return WindowsTextBox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    def create_textbox(self) -> TextBox:
        return MacTextBox()


##########################################################

def render_ui(factory: GUIFactory):
    btn = factory.create_button()
    txt = factory.create_textbox()
    btn.render()
    txt.render()

# Using Windows UI
render_ui(WindowsFactory())

# Using Mac UI
render_ui(MacFactory())


#OUTPUT:
# Rendering Windows-style Button
# Rendering Windows-style TextBox
# Rendering Mac-style Button
# Rendering Mac-style TextBox

#
# 🔹 Explanation
# 	•	Client code (render_ui) does not change whether it’s Windows or Mac.
# 	•	You just pass a different factory, and the right family of products is created.
# 	•	This is exactly what “Encapsulates object creation” means — client never deals with WindowsButton or MacTextBox directly.

#
# ✅ Factory Method Pattern
#
# “A pattern that creates one object through a factory method, letting subclasses decide which class to instantiate.”
#
# ⸻
#
# ✅ Abstract Factory Pattern
#
# “A pattern that creates a family of related objects through a factory, without specifying their concrete classes.”