from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Hello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint=(0.6,0.7)
        self.window.pos_hint ={"center_x":0.5,"center_y":0.5}
        #image widget
        self.window.add_widget(Image(source="Micheal.jpg"))
        
        #label widget
        self.greeting = Label(  
                            text="Whaasssuppp",
                            font_size = 20,
                            color = 'cyan'
                                )
        self.window.add_widget(self.greeting)
        
        #text input widget
        self.user = TextInput(
                            multiline=False,
                            padding_y = (10,10),
                            size_hint=(0.5,0.3),
                            )
        self.window.add_widget(self.user)
        
        #button widget
        self.button = Button(
                            text="SIKEE",
                            size_hint = (0.6,0.4),
                            bold = True,
                            background_color = "gray")
        self.button.bind(on_press= self.callback)
        self.window.add_widget(self.button)
        
        return self.window
    
    def callback(self,instance):
        self.greeting.text = "Hellooo " + self.user.text + "!"
        
    

if __name__ == "__main__":
    Hello().run()