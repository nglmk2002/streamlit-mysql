import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time

def main():
    # name = st.text_input('이름을 입력해주세요')
    # date_put = st.date_input('날짜입력')
    # time_put = st.time_input('시간입력')
    # birth_df = datetime.combine(date_put,time_put)
    # print(date_put)
    # print(time_put)
    
    if st.button('저장') :

        try :
            # 1. 커넥터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.cwppjkosdoqm.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = 'yh1234'
            )
            if connection.is_connected() :
                db_info = connection.get_server_info()
                print("MySQL server version : ", db_info)
                # 2. 커서를 가져온다.
                cursor = connection.cursor()
                # 3. 우리가 원하는거 실행가능
                query = """ insert into cats4(name,age) 
                            values (%s,%s); """
            
                record = [('냐웅이',1),('나비',3),('단비',5)]
                print(datetime.now())
                #cursor.execute(query,record)
                cursor.executemany(query,record)
                connection.commit()
                print("{}개 적용됨".format(cursor.rowcount))
                # 4. 실행 후 커서에서 결과를 빼낸다.
                #record = cursor.fetchone()
                #print('Connected to db : ',record)
        
        except Error as e :
            print('디비 관련 에러 발생',e)
        
        finally :
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면 커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')
if __name__ == '__main__' :
    main()



 # menu = ['DataBase 정보입력']
    # choice = st.sidebar.selectbox('메뉴',menu)
    # if choice == 'DataBase 정보입력' :
    #     title = st.text_input('타이틀을 입력해주세요')
    #     author_fname = st.text_input('성을 입력해주세요')
    #     author_lname = st.text_input('이름을 입력해주세요')
    #     released_year = st.number_input('출판년도를 입력해주세요',1,10000)
    #     stock_quantity = st.number_input('stock_quantity를 입력해주세요',1,10000)
    #     pages = st.number_input('페이지수를 입력해주세요',1,10000)
        