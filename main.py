from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Programme lair')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Summary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    link = db.Column(db.String(300))


    def __repr__(self):
        return f'Product{self.id}. {self.title}: {self.link}'


@app.route('/')
def main():
    repositories = Summary.query.all()
    return render_template('index.html', repository_list=repositories)

@app.route('/add', methods=['POST'])
def add_product():
    data = request.json
    resume = Summary(**data)
    db.session.add(resume)
    db.session.commit()

    global repositories
    id_last = repositories[-1]['id']
    id_new = id_last + 1
    data['id'] = id_new
    repositories.append(data)

    return 'OK'

@app.route('/clear', methods=["POST"])
def clear_experience():
    Summary.query.delete()
    db.session.commit()
    return 'Cleared successfully!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
