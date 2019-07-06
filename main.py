#! -*- coding: utf-8 -*-
__author__ = "Desnown"
__date__ = '06/2019'


#CONFIG
from kivy.config import Config
Config.set('graphics', 'borderless', True)
Config.set('kivy', 'exit_on_escape', False)
Config.set('kivy', 'resizable', True)


#KIVY
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.core.window import Window


#KIVYMD
from kivymd.theming import ThemeManager
from kivymd.button import MDFillRoundFlatButton
# from kivymd.label import MDLabel

#OTHERS
from pdb import set_trace #DEBUG
from tools_audio import read_info

#VARIABLES
cor_default = [.776, .157, .157, 1]
cor_default_2 = [.773, .239, .239, 1]


class Main(ScreenManager):
    pass


class Init(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.option)

    def option(self, window, key, *args):
        if key == 27:
            self.sair()
            return True

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
        yes = MDFillRoundFlatButton(text='Sim',
                                    on_release=App.get_running_app().stop,
                                    _radius=dp(14))

        no = MDFillRoundFlatButton(text="Não", on_release=pop.dismiss,
                                    _radius=dp(14))

        botoes.add_widget(yes)
        botoes.add_widget(no)

        box.add_widget(img)
        box.add_widget(botoes)

        aumentar_tela = Animation(size=(300,180), t='out_back', d=.4)
        aumentar_tela.start(pop)

        pop.open()
        return True    


class Old(Screen):
    def on_enter(self):
        # self.ids.bx_sc.clear_widgets()
        self.printar_dados()

    def printar_dados(self):
        datas = read_info()

        for item in datas:
            self.ids.bx_sc.add_widget(MYLabel(text=item, size_hint=[1, None], height=30))
            

class New(Screen):
    def animation_up(self):
        change_pos = Animation(pos_hint={'center_y': .505}, d=.3)
        change_size = Animation(size=(dp(70), dp(70)), d=.3, t='linear', pos_hint= {'right': .995})

        change_pos.start(self.ids.bx_record)
        change_size.start(self.ids.microphone)


    def animation_down(self):
        change_pos = Animation(pos_hint={'center_y': .525}, d=.3)
        change_size = Animation(size=(dp(50), dp(50)),t='linear',  d=.3, pos_hint={'right': .975})

        change_pos.start(self.ids.bx_record)
        change_size.start(self.ids.microphone)


    
class Audio_Text(App):
    title = 'Audio Text'
    icon = 'Imagens/main.jpeg' 
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Red'
    theme_cls.primary_hue = '800'
    theme_cls.theme_style = 'Dark'


    def build(self):
        return Main()

    # def on_stop(self):
    #     window_size = Animation(size_hint=(1000,700), t='out_back', d=.4)
    #     window_size.start(Init)


Audio_Text().run()
