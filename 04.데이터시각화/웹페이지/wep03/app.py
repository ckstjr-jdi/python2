from flask import Flask, render_template
import pandas as pd
df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv')


app = Flask(__name__, template_folder='temp')

@app.route('/')
def index():
    df1 = df[['지원번호', '이름', '학교', '키', 'SW특기']]
    df1.set_index('지원번호')
    df2 = df[['지원번호', '이름', '국어', '영어', '수학', '과학', '사회']]
    df2.set_index('지원번호')

    info = df1.to_html(classes="table table-striped table-hover", index=False)
    score = df2.to_html(classes="table table-striped",index=False)
    return render_template('index.html', info=info, score=score)

if __name__=='__main__':
    app.run(port=5000, debug=True)
