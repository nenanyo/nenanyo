
import cx_Oracle

# --------------------------------------
# 상품목록
# --------------------------------------
def goods_list () :
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "select * from KIO_GOODS"
    cur = conn.cursor()
    cur.execute(sql)
    for row in cur:
        print(list(row))
    cur.close()
    conn.close()


#--------------------------------------
# 카트담기
# insert into KIO_CART(CART_SEQ,TEL,GOOD_SEQ,GOOD_PRICE,ORDER_AMOUNT,ORDER_PRICE,REG_DATE)
#  values(KIO_CART_SEQ.nextval, '0505', 1, 1000, 2, 2000, sysdate);
#--------------------------------------
def cart_add(tel, GOOD_SEQ, GOOD_PRICE, ORDER_AMOUNT, ORDER_PRICE)  :
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = '''insert 
             into KIO_CART(CART_SEQ,TEL,GOOD_SEQ,GOOD_PRICE,ORDER_AMOUNT,REG_DATE)
             values(KIO_CART_SEQ.nextval, :1, :2, :3, :4, sysdate)'''
    cur = conn.cursor()
    cur.execute(sql, [tel, GOOD_SEQ, GOOD_PRICE, ORDER_AMOUNT])
    conn.commit()
    cur.close()
    conn.close()


# --------------------------------------
# 상품주문
#  insert into kio_order(ORDER_SEQ,TEL,ORDER_PRICE,PAY_GUBUN,REG_DATE)
#  values (kio_order_seq.nextval, '0505',  4500, '1', sysdate)
# --------------------------------------
def orders(TEL,ORDER_PRICE,PAY_GUBUN):
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = ''' insert into kio_order(ORDER_SEQ,TEL,ORDER_PRICE,PAY_GUBUN,REG_DATE)
            values (kio_order_seq.nextval, :1, :2, :3, sysdate)'''
    cur = conn.cursor()
    cur.execute(sql, [TEL, ORDER_PRICE, PAY_GUBUN])
    conn.commit()
    cur.close()
    conn.close()


# goods_list ()
# cart_add('0505', 1, 1000, 2, 2000)
orders('0505', 4500, '1')

