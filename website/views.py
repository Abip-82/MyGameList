from flask import Blueprint , render_template , request
from flask_login import login_required , current_user
from dotenv import load_dotenv
import os , requests
from . import db
from .models import Game, Collection

load_dotenv()

views = Blueprint("views" ,__name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/games" , methods = ['GET','POST'])
@login_required
def games():
    games = []
    if request.method == "POST":
        search = request.form.get("search").strip()
        response = requests.get("https://api.rawg.io/api/games",params={"key":os.getenv("RAWG_API_KEY"),"search":search})
        data = response.json()
        games = data.get("results",[])
    return render_template("games.html", games = games)

@views.route("/addgame" , methods = ['POST'])
@login_required
def addgame():
    title = request.form.get("title")
    api_id = request.form.get("api_id")

    game = Game.query.filter_by(api_id=api_id).first()
    if not game:
        game = Game(title=title, api_id=api_id)
        db.session.add(game)
        db.session.commit()
    
    existing = Collection.query.filter_by(user_id=current_user.id, game_id =game.id).first()
    if existing:
        return f"{title} already exists in your collection"
    collection = Collection(status="Want to Play", user_id = current_user.id, game_id =game.id)
    db.session.add(collection)
    db.session.commit()
    return f"Added {title} to your collection"
