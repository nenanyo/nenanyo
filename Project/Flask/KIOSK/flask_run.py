from flask import Flask,session, render_template, make_response, jsonify, request, redirect, url_for
import cx_Oracle
import random
app = Flask(__name__)

app.secret_key = "1111122222"


@app.route('/')
def index():
    tel = str(random.randint(10, 99)) + str(random.randint(10, 99))
    session['MY_TEL_SESSION'] = tel
    return render_template('/index.html')

@app.route('/menu')
def menu():
    conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
    sql = """select GOOD_SEQ,GOOD_NAME,GOOD_IMG,GOOD_PRICE,GOOD_DESC
    from KIO_GOODS order by reg_date desc"""
    cur = conn.cursor()
    cur.execute(sql)
    goods_list_dict = []
    for row in cur:
        dic = {}
        dic["GOOD_SEQ"]=row[0]
        dic["GOOD_NAME"]=row[1]
        dic["GOOD_IMG"]=row[2]
        dic["GOOD_PRICE"]=row[3]
        dic["GOOD_DESC"]=row[4]
        goods_list_dict.append(dic)
    cur.close()
    conn.close()
    return render_template('menu.html', KEY_GOODS_LIST_DICT=goods_list_dict)

@app.route('/detail_view', methods =['get'])
def detail_view():
    prm_good_seq = request.args.get('prm_good_seq')
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """select GOOD_SEQ,GOOD_NAME,GOOD_IMG,GOOD_PRICE,GOOD_DESC
                from kio_goods where good_seq= :1
    """
    cur = conn.cursor()
    cur.execute(sql,[prm_good_seq])
    goods_list_dict = []
    for row in cur:
        dic = {}
        dic["GOOD_SEQ"] = row[0]
        dic["GOOD_NAME"] = row[1]
        dic["GOOD_IMG"] = row[2]
        dic["GOOD_PRICE"] = row[3]
        dic["GOOD_DESC"] = row[4]
        goods_list_dict.append(dic)
    cur.close()
    conn.close()
    return render_template('product-single.html',KEY_GOODS_LIST_DICT = goods_list_dict)

def my_cart_list():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """select g.GOOD_SEQ, g.GOOD_NAME, g.GOOD_IMG, g.GOOD_DESC,
                      c.GOOD_PRICE,  c.ORDER_AMOUNT
                     , (c.GOOD_PRICE*c.ORDER_AMOUNT) as TOT_PRICE,c.CART_SEQ
                       from KIO_GOODS g,  KIO_CART c where g.GOOD_SEQ = c.GOOD_SEQ and TEL = :1
            """
    cur = conn.cursor()
    cur.execute(sql,[session['MY_TEL_SESSION']])
    goods_list_dict = []
    total_price = 0
    for row in cur:
        dic = {}
        dic["GOOD_SEQ"] = row[0]
        dic["GOOD_NAME"] = row[1]
        dic["GOOD_IMG"] = row[2]
        dic["GOOD_DESC"] = row[3]
        dic["GOOD_PRICE"] = row[4]
        dic["ORDER_AMOUNT"] = row[5]
        dic["TOT_PRICE"] = row[6]
        dic["CART_SEQ"] = row[7]
        total_price = total_price + int(row[6])
        goods_list_dict.append(dic)
    cur.close()
    conn.close()
    return [goods_list_dict, total_price]


@app.route('/add_cart', methods = ['post'])
def add_cart():
    v_good_seq = request.form.get("good_seq")
    v_good_price = request.form.get("good_price")
    v_amount = request.form.get("amount")

    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """ insert into
            KIO_CART(CART_SEQ, TEL, GOOD_SEQ, GOOD_PRICE, ORDER_AMOUNT, REG_DATE)
            values(KIO_CART_SEQ.nextval, :1, :2, :3, :4, sysdate)"""
    cur = conn.cursor()
    cur.execute(sql, [session['MY_TEL_SESSION'], v_good_seq, v_good_price, v_amount])
    conn.commit()
    cur.close()
    conn.close()
    MY_CART_LIST = my_cart_list()
    return render_template('cart.html', KEY_GOODS_LIST_DICT=MY_CART_LIST[0], KEY_TOTAL=MY_CART_LIST[1])

@app.route('/cart_delect',methods = ['get'])
def cart_delect():
    v_cart_seq=request.args.get('prm_cart_seq')
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = 'delete from KIO_CART where cart_seq = :1'
    cur = conn.cursor()
    cur.execute(sql, [v_cart_seq])
    conn.commit()
    cur.close()
    conn.close()
    MY_CART_LIST = my_cart_list()
    return render_template('cart.html',KEY_GOODS_LIST_DICT =MY_CART_LIST[0], KEY_TOTAL=MY_CART_LIST[1])

@app.route('/orders',methods = ['get'])
def ordesrs():
    prm_total = request.args.get('prm_total')
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """insert into
        kio_order(ORDER_SEQ,TEL, ORDER_PRICE, PAY_GUBUN, REG_DATE)
        values(kio_order_seq.nextval, :1, :2, '1', sysdate)"""
    cur = conn.cursor()
    cur.execute(sql,[session['MY_TEL_SESSION'], prm_total])
    conn.commit()
    return redirect("/")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)