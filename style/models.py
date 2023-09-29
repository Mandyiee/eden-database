from app import db
import uuid
import datetime
from pygments import highlight
from pygments.formatters import HtmlFormatter
from sqlalchemy import event
from pygments.lexers import Python3Lexer, guess_lexer, get_lexer_by_name, TextLexer

class Image(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False,index=True)
    image_file = db.Column(db.String(128),nullable=True)
    code = db.Column(db.Text,nullable=True,default="print('HELLO WORLD')")
    highlighted_code = db.Column(db.Text,nullable=True)
    style_definitions = db.Column(db.Text,nullable=True)
    style_bg_color = db.Column(db.String(128),nullable=True)
    lexer = db.Column(db.String(64),nullable=True,default="Text")
    current_lang = db.Column(db.String(64),nullable=True,default="Text")
    style = db.Column(db.String(64),nullable=True,default="monokai")
    font = db.Column(db.String(64),nullable=True,default="'Playfair Display',serif")
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        if self.style is None:
            self.style = "monokai"
        if self.font is None:
            self.font = "'Playfair Display',serif"
        if self.current_lang is None:
            self.current_lang = "Text"
        
        
    def __repr__(self):
        return '<%r>' % self.id

def calculate_and_update_codes_lexer(target, value, oldvalue, initiator):
    if value != oldvalue:
        try:
            lexer = get_lexer_by_name(value)
            print(lexer)
        except Exception as e:
            lexer = TextLexer()
        formatter = HtmlFormatter(style=target.style)
        target.style_definitions = formatter.get_style_defs()
        target.style_bg_color = formatter.style.background_color
        target.highlighted_code = highlight(target.code, lexer, formatter)


def calculate_and_update_codes_style(target, value, oldvalue, initiator):
    if value != oldvalue:
        try:
            lexer = get_lexer_by_name(target.current_lang)
            print(lexer)
        except Exception as e:
            lexer = TextLexer()
        formatter = HtmlFormatter(style=value)
        target.style_definitions = formatter.get_style_defs()
        target.style_bg_color = formatter.style.background_color
        target.highlighted_code = highlight(target.code, lexer, formatter)
        

def calculate_and_update_codes_code(target, value, oldvalue, initiator):
    if value != oldvalue:
        try:
            if target.current_lang == None:
                lexer = get_lexer_by_name('Text')
                print(lexer)
            else:
                lexer = get_lexer_by_name(target.current_lang)
                print(lexer)
        except Exception as e:
            lexer = TextLexer()
        if target.style == None:
            formatter = HtmlFormatter(style='monokai')
        else:
            formatter = HtmlFormatter(style=target.style)
        target.style_definitions = formatter.get_style_defs()
        target.style_bg_color = formatter.style.background_color
        target.highlighted_code = highlight(value, lexer, formatter)
        

event.listen(Image.current_lang, 'set', calculate_and_update_codes_lexer)
event.listen(Image.style, 'set', calculate_and_update_codes_style)
event.listen(Image.code, 'set', calculate_and_update_codes_code)