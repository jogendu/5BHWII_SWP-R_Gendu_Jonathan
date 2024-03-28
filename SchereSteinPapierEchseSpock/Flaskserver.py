from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)


class SymbolCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    schere_count = db.Column(db.Integer, nullable=False)
    stein_count = db.Column(db.Integer, nullable=False)
    papier_count = db.Column(db.Integer, nullable=False)
    echse_count = db.Column(db.Integer, nullable=False)
    spock_count = db.Column(db.Integer, nullable=False)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/score", methods=["GET", "POST", "PUT", "DELETE"])
def score():
    if request.method == "POST":
        return set_score()
    elif request.method == "PUT":
        return update_score()
    elif request.method == "DELETE":
        return delete_score()
    else:  # GET
        return get_score()


@app.route("/symbols", methods=["GET", "POST", "PUT", "DELETE"])
def symbols():
    if request.method == "POST":
        return set_symbols()
    elif request.method == "PUT":
        return update_symbols()
    elif request.method == "DELETE":
        return delete_symbols()
    else:  # GET
        return get_symbols()


def set_score():
    data = request.json
    user_score, created = get_or_create(Score, user_name=data.get('user_name'))
    user_score.score = data.get('score', 0)
    db.session.commit()
    return "Score updated successfully!"


def get_score():
    user_name = request.args.get('user_name')
    user_score = Score.query.filter_by(user_name=user_name).first()
    if user_score:
        return f"User: {user_score.user_name}, Score: {user_score.score}"
    return "User not found!"


def update_score():
    data = request.json
    user_score = Score.query.filter_by(user_name=data.get('user_name')).first()
    if user_score:
        user_score.score += 200
        db.session.commit()
        return "Score updated successfully!"
    return "User not found!"


def delete_score():
    data = request.json
    user_score = Score.query.filter_by(user_name=data.get('user_name')).first()
    if user_score:
        db.session.delete(user_score)
        db.session.commit()
        return "Score deleted successfully!"
    return "User not found!"


def set_symbols():
    data = request.json
    user_symbols, created = get_or_create(SymbolCount, user_name=data.get('user_name'))
    for symbol in ['schere', 'stein', 'papier', 'echse', 'spock']:
        setattr(user_symbols, f"{symbol}_count", data.get(f'{symbol}_count', 0))
    db.session.commit()
    return "Symbols count updated successfully!"


def get_symbols():
    user_name = request.args.get('user_name')
    user_symbols = SymbolCount.query.filter_by(user_name=user_name).first()
    if user_symbols:
        return {symbol: getattr(user_symbols, f"{symbol}_count") for symbol in
                ['schere', 'stein', 'papier', 'echse', 'spock']}
    return "User not found!"


def update_symbols():
    data = request.json
    user_symbols = SymbolCount.query.filter_by(user_name=data.get('user_name')).first()
    if user_symbols:
        field_name = data.get('field_name')
        if hasattr(user_symbols, field_name):
            setattr(user_symbols, field_name, getattr(user_symbols, field_name) + 1)
            db.session.commit()
            return "Symbols count updated successfully!"
    return "User not found!"


def delete_symbols():
    data = request.json
    user_symbols = SymbolCount.query.filter_by(user_name=data.get('user_name')).first()
    if user_symbols:
        db.session.delete(user_symbols)
        db.session.commit()
        return "Symbols count deleted successfully!"
    return "User not found!"


def get_or_create(model, **kwargs):
    instance = model.query.filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        instance = model(**kwargs)
        db.session.add(instance)
        return instance, True


if __name__ == "__main__":
    app.run()
