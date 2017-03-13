from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class ButtonMaker(GridLayout):
	buttons = {}
	for i in range(9):
		buttons[str(i+1)] = str(i+1)

	def do_press(self, num):
		filename = "Sounds/audio" + self.buttons[num] + '.wav'
		sound = SoundLoader.load(filename)
		sound.play()


class SoundPanelApp(App):
	def build(self):
		return ButtonMaker()

if __name__ == "__main__":
	SoundPanelApp().run()