from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# 운동기록 DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wodrecords.db'  # 데이터베이스 파일 이름
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 경고 제거
# 1rm DB
app.config['SQLALCHEMY_BINDS'] = {
    'newdb': 'sqlite:///newdb.db'
}
db = SQLAlchemy(app)

# 운동 기록 모델
class WodRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    wod = db.Column(db.String(100), nullable=False)
    scale = db.Column(db.String(200), nullable=True)
    memo = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"WodRecord('{self.date}', '{self.wod}')"

# 1rm 모델
class PrList(db.Model):
    __bind_key__ = 'newdb' # 새 db 사용

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    date = db.Column(db.String(100), nullable=False)
    record = db.Column(db.float, nullable=False)

    def __repr__(self):
        return f"<Exercise '{self.name}'>"

# db 생성
with app.app_context():
    db.create_all()

    # 데이터가 비어 있으면 샘플 데이터를 추가
    if not WodRecord.query.first():  # 데이터가 없으면 추가
        new_record = WodRecord(date="2025-03-28", title='히어로와드', wod="머프", scale="10", memo="매우 힘듬")
        db.session.add(new_record)
        db.session.commit()

# 홈화면
@app.route('/')
def index():
    records = WodRecord.query.limit(3).all()  # DB에서 모든 기록 가져오기
    return render_template('index.html', records=records)

@app.route('/save', methods=['POST'])
def save():
    # 폼에서 데이터 받기 
    date = request.form['date']
    title = request.form['title']
    wod = request.form['wod']
    scale = request.form.get('scale', '')
    memo = request.form['memo']

    # 새 기록을 db에 추가
    new_record = WodRecord(date=date, title=title, wod=wod, scale=scale, memo=memo)
    db.session.add(new_record)
    db.session.commit()

    return redirect('/')  # 저장 후 다시 홈으로 리다이렉트

# 기록 목록 페이지
@app.route('/records')
def record_list():
    records = WodRecord.query.all()
    return render_template('record_list.html', records=records)


# 기록 상세 보기
@app.route('/record/<int:id>')
def record(id):
    record = WodRecord.query.get_or_404(id)
    return render_template('record_detail.html', record=record)

# 기록 삭제 라우트
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    record = WodRecord.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()

    return redirect('/')  # 삭제 후 홈으로 리다이렉트

# 1rm 기록하기
@app.route('/pr', methods=['GET', 'POST'])
def new_record():


if __name__ == '__main__':
    app.run(debug=True)
