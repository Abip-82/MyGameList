from flask import Blueprint , render_template , request
from flask_login import login_required
from dotenv import load_dotenv
import os , requests



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
    return f"Added {title} to your collection"
