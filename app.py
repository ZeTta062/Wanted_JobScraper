from flask import Flask, render_template, request, redirect, send_file
from scraper import scrape_jobs
from file import save_to_file


app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = scrape_jobs(keyword)
        db[keyword] = jobs
    job_count = len(jobs)


    return render_template(
        "search.html", 
        keyword=keyword,
        jobs=jobs,
        job_count=job_count
    )

@app.route("/export")           # export?keyword=파이썬
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)
    

app.run(debug=True)
# app.run("0.0.0.0") 레플릿 실행시 코드