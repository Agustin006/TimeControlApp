## App
from datetime import datetime as dt
import pandas as pd
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
"La idea de esta App es que pueda ser facil traquear mi tiempo de estudio. Tiene que ser lo suficientemente flexible para poder agregar projectos y con dos botnoes agregar y  eliminar prjectos"

projects = []

def project(func):
        "deberia tener la posibilidad de poder VER los actuales proyectos, Agregar proyectos o eliminar proyectos, modificar"
        def add(): #Agregar proyectos
            try:
                x = input("Que proyecto desea agregar: ")
                projects.append(x)
            except:
                print("There is a problem")
        def delete(): #Eliminar proyecto
            x = input(print("what project do yo want to delete?", projects))
            projects.remove(x)


start = dt.now()
end = dt.now()
duration = end - start


## Kivy


## App class es la que nso permite abrir uan ventan. Y tiene un Run method.
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 4
        self.add_widget(Label(text="Select a process"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)


        #Crear boton start
        self.start = Button(text="Start")
        self.start.bind(on_press=self.pressed) #binding para que el boton funcione
        self.add_widget(self.start)


        self.finish = Button(text="Finish")
        self.add_widget(self.finish)

    #Hbailito una habilidad para la funcion.
    def pressed(self, instance):
        print(start)
        print("ok")

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
