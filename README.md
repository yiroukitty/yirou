# yirou's Diary

##介紹

嘗試做網頁。

##成果展示

![](https://github.com/yiroukitty/yirou/raw/master/demo.png)

##使用技術

名稱    |    說明
--------|-----------
Python  | 使用最多的 !
Flask   | 幫我架設網站的功臣
repl.it | 線上寫程式環境
Heroku  | 免費放網站的公司
Github  | 真正的佛心企業

##範例代碼

ˋˋˋ@app.route("/")
def root():
  ds = glob.glob("articles/*")
  result = []
  for d in ds:
    fs = glob.glob(d + "/*.txt")
    t = (d.split("/")[-1], len(fs))
    result.append(t)
  return render_template("index.html",d = result)
ˋˋˋ
