import os
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
from utils.resume_parser import parse_resume_pdf
from utils.ai import generate_resume_feedback, match_jobs

ALLOWED_EXTENSIONS = {"pdf"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "changeme")
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/resumematch")

    mongo = PyMongo(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/upload", methods=["POST"])
    def upload():
        if "resume" not in request.files:
            flash("No file part")
            return redirect(url_for("index"))
        file = request.files["resume"]
        if file.filename == "":
            flash("No selected file")
            return redirect(url_for("index"))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join("uploads", filename)
            os.makedirs("uploads", exist_ok=True)
            file.save(save_path)

            parsed = parse_resume_pdf(save_path)
            feedback = generate_resume_feedback(parsed)

            resume_id = mongo.db.resumes.insert_one({
                "filename": filename,
                "parsed": parsed,
                "feedback": feedback,
                "created_at": datetime.datetime.utcnow()
            }).inserted_id

            jobs = match_jobs(parsed, mongo.db.jobs.find({}))

            return render_template("dashboard.html", feedback=feedback, jobs=jobs)

        flash("Allowed file type: pdf")
        return redirect(url_for("index"))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
