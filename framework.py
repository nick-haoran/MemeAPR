import json
from cnstd import CnStd
from cnocr import CnOcr

db={"filename":{
    "history":[
        {
            "keywords":[],
            "text_emb":[],
            "text_emoscore":[]
        },
        {
            "keywords":[],
            "text_emb":[],
            "text_emoscore":[]
        }
    ],
    "ocr":{
        "keywords":[],
        "text_emb":[],
        "text_emoscore":[]
    },
    "graph_emoscore":[]

}}

def generate_record(s:str):
    t={
        "keywords":get_keywords(s),
        "text_emb":get_text_emb(s),
        "text_emoscore":text_emotion_evaluate(s)
    }
    return t


def init():
    pass


def main():
    try:
        init()
        ...
    except BaseException:
        on_exception()


def on_callback():
    pass


def on_exception():
    pass


def predict_text(s:str):
    pass


def get_text_emb(s:str):
    pass


def text_emotion_evaluate(s:str):
    pass


def graph_emotion_evaluate(dir:str):
    pass


def get_keywords(s:str):
    pass


def cmp_cos(a:list,b:list):
    pass


def cmp_jac(a:list,b:list):
    pass


def ocr(dir:str):
    pass

