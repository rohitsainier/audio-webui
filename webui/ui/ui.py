import gradio as gr
from .tabs import *

tabs_el: gr.Tabs = None


def create_ui(theme) -> gr.Blocks:

    from simplestyle.manager import create_stylesheet, SimpleStyle, StyleRule, StyleValue

    with SimpleStyle(priority=0):
        with StyleRule('.gradio-container'):
            StyleValue('max-width', 'calc(100% - 100px) !important')

        with StyleRule('.tabitem:not(.tabitem .tabitem)'):
            StyleValue('height', 'calc(100vh - 100px) !important')
            StyleValue('overflow', 'auto')

        with StyleRule('.tool'):
            StyleValue('max-width', '2.2em')
            StyleValue('min-width', '2.2em !important')
            StyleValue('height', '2.4em')
            StyleValue('align-self', 'end')
            StyleValue('line-height', '1em')
            StyleValue('border-radius', '0.5em')

        with StyleRule('.smallsplit'):
            StyleValue('max-width', '2.2em')
            StyleValue('min-width', '2.2em !important')
            StyleValue('align-self', 'end')
            StyleValue('border-radius', '0.5em')

        with StyleRule('.offset--10'):
            StyleValue('transform', 'translateY(-10px)')

        with StyleRule('.text-center'):
            StyleValue('text-align', 'center')

        with StyleRule('.padding-h-0'):
            StyleValue('padding-left', '0 !important')
            StyleValue('padding-right', '0 !important')

        with StyleRule('table:not(.file-preview)'):
            StyleValue('border', '1px solid white !important')
            StyleValue('margin-left', 'auto')
            StyleValue('margin-right', 'auto')

        with StyleRule('table a'):
            StyleValue('color', 'white !important')

        with StyleRule('table th, table td'):
            StyleValue('padding', '10px !important')

        with StyleRule('.center-h'):
            StyleValue('margin-left', 'auto !important')
            StyleValue('margin-right', 'auto !important')
            StyleValue('text-align', 'center !important')


    tabs = [
        ('📜▶🗣 Text to speech', text_to_speech),
        ('🗣▶🗣 RVC', rvc),
        ('📜▶🎵 AudioLDM', audioldm_tab),
        ('📜▶🎵 AudioCraft', audiocraft_tab),
        ('🗣▶📜 Whisper', whisper),
        ('🧨 Train', training_tab),
        ('🔨 Utils', utils_tab),
        ('⚙ Settings', extra_tab),
        ('🧾 Info', info_tab)
    ]
    global tabs_el
    with gr.Blocks(theme=theme, title='🔊Audio WebUI🎵', css=create_stylesheet()) as webui:
        with gr.Tabs() as tabs_element:
            tabs_el = tabs_element
            for name, content in tabs:
                with gr.Tab(name, id=name):
                    content()
    return webui
