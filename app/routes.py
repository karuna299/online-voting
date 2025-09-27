from flask import Blueprint, render_template, request, redirect, current_app

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vote = request.form.get("vote")
        if vote in ["cats", "dogs"]:
            current_app.redis.incr(vote)
        return redirect("/results")

    cats = int(current_app.redis.get("cats") or 0)
    dogs = int(current_app.redis.get("dogs") or 0)
    return render_template("index.html", cats=cats, dogs=dogs)


@main.route("/results")
def results():
    cats = int(current_app.redis.get("cats") or 0)
    dogs = int(current_app.redis.get("dogs") or 0)
    return render_template("results.html", cats=cats, dogs=dogs)
