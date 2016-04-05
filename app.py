#coding:utf-8
import config
from flask import Flask, render_template, request
import MeCab

app=Flask(__name__)
app.debug=True

mecab = MeCab.Tagger('-Owakati -d %s' % (config.mecab_dic_dir))
#mecab = MeCab.Tagger('-Owakati')

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/realy', methods=['POST'])
def realy():
    text = request.form['text']
    wakati=mecab.parse(text)
    words=wakati.split(" ")
    result=""
    for word in words:
        result+="#"
        result+=str(word)
        result+=" "
    result=result[:len(result)-3]
    return str(result)



if __name__=="__main__":
    app.run()
