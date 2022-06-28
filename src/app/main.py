from flask import Flask,render_template,request,redirect,url_for
from .jpstock import JapanStock

app = Flask(__name__)

@app.route("/")
def main():
    return "project start"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/jp_stock")
def display_jp_page():
    return render_template("jp_stock.html")

@app.route("/us_stock")
def display_us_page():
    return render_template("us_stock.html")

@app.route("/get_js_stock",methods=["GET"])
def get_js_stock():
    
    try:
        stock_code = request.args.get("stockcode")
        jp_stock = JapanStock(stock_code)
        df = jp_stock.getJpStock()
    
        return render_template("jp_stock.html",stockcode=stock_code,dataframe = df ,method=request.method)
    except Exception as err:
        print(err)
        return render_template("jp_stock.html")

@app.route("/get_us_stock",methods=["GET"])
def get_us_stock():
    ticker = request.args.get("ticker")

    return render_template("us_stock.html",ticker=ticker,method=request.method)

if __name__ == "__main__":
    app.run(debug=True)