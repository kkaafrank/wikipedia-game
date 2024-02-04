"""
"""
import PySimpleGUI as sg

from constants import config


def get_game_inputs() -> dict:
    gui_layout: list[list[sg.Element]] = create_game_setup_layout()
    gui_window: sg.Window = sg.Window(title='Setup the Game', layout=gui_layout)
    event, values = gui_window.read()
    gui_window.close()

    return process_gui_inputs(event, values)


def create_game_setup_layout() -> list[list[sg.Element]]:
    input_field_size: tuple[int, int] = (64, 1)
    layout: list[list[sg.Element]] = [
        [sg.Text('Start Link:', expand_x=True), sg.Input(key='start_link', size=input_field_size)],
        [sg.Text('End Link:', expand_x=True), sg.Input(key='end_link', size=input_field_size)],
        # TODO: browser vs no browser mode
        # TODO: difficult: time between processing links
        [sg.Cancel(key='cancel'), sg.Ok(key='ok')]
    ]

    return layout


def process_gui_inputs(event: str, values: dict) -> dict:
    if event == 'cancel' or event == sg.WINDOW_CLOSED:
        return {}

    start_link: str = values['start_link']
    end_link: str = values['end_link']
    en_wiki_substr: str = config['WIKIPEDIA_URL_SUBSTR']
    if en_wiki_substr not in start_link or en_wiki_substr not in end_link:
        sg.popup_ok(f'"{en_wiki_substr}" must be a part of both links')
        return {}
