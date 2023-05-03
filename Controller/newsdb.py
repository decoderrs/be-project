import pandas as pd

class newsDb:
    def __init__(self,cursor,mydb):
        self.cursor = cursor
        self.mydb = mydb

    def create(self):
        sql = "INSERT INTO news (stock_name, sentiment, prev_close, pred_price) VALUES (%s, %s, %s, %s )"

        val = pd.read_csv('static/dummydata.csv').drop(columns=['Unnamed: 0']).to_dict('list')
        lst = []

        for row in range(len(val['Stock'])):
            newsObj = newsObject(val['Stock'][row], val['Sentiment'][row], val['Previous Close'][row], val['Predicted Price'][row])
            thisset = tuple((newsObj.stock,newsObj.sentiment,newsObj.prev_close,newsObj.pred_price))
            lst.append(thisset)

        #print(val)
        #print(lst)

        self.cursor.executemany(sql, lst)
        self.mydb.commit()

        #print(self.cursor.rowcount, ' was inserted')

        return lst

    def read_news(self):

        self.cursor.execute('SELECT * FROM news')

        result = self.cursor.fetchall()

        res = {}

        for i in result:
            if i[1] not in res:
                res[i[1]] = i

        #for x in result:
        #    print(x[0],' ', x[1], ' ', x[2], ' ', x[3], ' ', x[4], ' ')

        print(list(res.values())[:5])
        return list(res.values())[:5]

    def delete_news(self):

        sql = "DELETE FROM news"

        self.cursor.execute(sql)

        self.mydb.commit()

        print(self.cursor.rowcount, " records are deleted")


class newsObject:

    def __init__(self,stock,sentiment,prev_close,pred_price):
        self.stock = stock
        self.sentiment = sentiment
        self.prev_close = prev_close
        self.pred_price = pred_price