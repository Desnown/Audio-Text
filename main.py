#! -*- coding: utf-8 -*-


#CONFIG
from kivy.config import Config
Config.set('graphics', 'borderless', True)
Config.set('kivy', 'exit_on_escape', False)


#KIVY
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.metrics import dp

#KIVYMD
from kivymd.theming import ThemeManager
from kivymd.button import MDFillRoundFlatButton

#OTHERS
# from pdb import set_trace #DEBUG

#VARIABLES
cor_default = [.776, .157, .157, 1]


Window.clearcolor = [0,0,0, 1]


class Main(ScreenManager):
    pass


class Init(Screen):
    def sair(self, *args, **kw):
        box = BoxLayout(orientation="vertical", padding=10, spacing=10)
        botoes = BoxLayout(padding=(35,7), spacing=10)
        pop = Popup(title='Deseja mesmo sair ?',
                    content=box,
                    size_hint=(None, None),
                    size=(200,200),
                    separator_color=cor_default,
                    title_align='center',
                    auto_dismiss=True,
                    title_color=[1,1,1,1],
                    background='Imagens/pop.png')

        img = Image(source='Imagens/att.png')
        yes = MDFillRoundFlatButton(text='Sim', on_release=App.get_running_app().stop, _radius=dp(14))
        no = MDFillRoundFlatButton(text="Não", on_release=pop.dismiss, _radius=dp(14))

        botoes.add_widget(yes)
        botoes.add_widget(no)

        box.add_widget(img)
        box.add_widget(botoes)

        aumentar_tela = Animation(size=(300,180), t='out_back', d=.4)
        aumentar_tela.start(pop)

        pop.open()
        return True    


class Old(Screen):
    def olds(self):
        pass

    
class Audio_Text(App):
    title = 'Audio Text'
    icon = 'Imagens/main.jpeg' 
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Red'
    theme_cls.primary_hue = '800'
    theme_cls.theme_style = 'Dark'


    def build(self):
        return Main()


Audio_Text().run()