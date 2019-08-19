#開啟伺服器
from flask import Flask
from flask import render_template
import glob
import os
from datetime import datetime

#網頁名稱
app = Flask("Kitty")
#若執行首頁就執行以下
@app.route("/")
def root():
  ds = glob.glob("articles/*")
  result = []
  for d in ds:
    fs = glob.glob(d + "/*.txt")
    t = (d.split("/")[-1], len(fs))
    result.append(t)
  return render_template("index.html",d = result)

@app.route("/category/<c>")
def catergory(c):
  fs = glob.glob("articles/" + c + "/*.txt")
  result = []
  for i, f in enumerate(fs):
    fsplit = f.split("/")[-1].replace(".txt", "")
    a = open(f)
    article = a.read()
    a.close()
    m = os.path.getmtime(f)
    mstr = str(datetime.utcfromtimestamp(m))
    #座號，名稱，十
    t = (i, fsplit, mstr, article)
    result.append(t)
  return render_template("category.html", d = result)




#run網頁
if __name__ == "__main__":
  app.run(debug=True, port='3000', host='0.0.0.0')
