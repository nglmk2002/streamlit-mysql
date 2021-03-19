import streamlit as st
import mysql.connector
from mysql.connector import Error
import numpy as np
import pandas as pd
import json


def main():
    st.subheader('책 정보 데이터')
    menu = ['Books data','Select','Update','Delete']
    choice = st.sidebar.selectbox('Books Data,Select,Update,Delete',menu)
 
    if choice == 'Books data':
        book_id_list = []
        try :
            connection = mysql.connector.connect(
                host = 'database-1.cwppjkosdoqm.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = 'yh1234'
            )
            if connection.is_connected() :
                cursor = connection.cursor(dictionary=True)
                query = """select * from books limit 5 ;"""
                cursor.execute(query)
                results = cursor.fetchall()
                
                for row in results:
                    st.write(row)
                    book_id_list.append(row['book_id'])
                            


        except Error as e :
                print('디비 관련 에러 발생',e)
            
        finally :
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면 커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')
    if choice == 'Select':
        try:
            connection = mysql.connector.connect(
                host = 'database-1.cwppjkosdoqm.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = 'yh1234'
            )
    
        
            if connection.is_connected() :
                cursor = connection.cursor(dictionary=True)
                select_box = ['book_id','title','author_fname','author_lname','released_year','stock_quantity','pages']
                select_column = st.multiselect('원하는 컬럼을 선택해주세요',select_box)
                if len(select_column) == 0:
                    query = """select * from books limit 5 ;"""
                else :
                    column_str = ','.join(select_column)
                    query = "select book_id," + column_str+ " from books limit 5 ;"
                cursor.execute(query)
                results = cursor.fetchall()
                #st.write(type(results))
                #파이썬의 리스트+딕셔너리 조합을 =>json형식으로 바꾸는것.
                json_results = json.dumps(results)
                # 판다스의 데이터프레임으로 읽기.
                df=pd.read_json(json_results)
                st.dataframe(df)

                # st.write(type(json_results))
                # st.write(json_results)
                # for row in results:
                #     st.write(row)
                

        except Error as e :

            print('디비 관련 에러 발생',e)
            
        finally :
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면 커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')


    if choice == 'Delete':
        book_id_list=[]   
        try :
            # 1. 커넥터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.cwppjkosdoqm.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = 'yh1234'
            )
            if connection.is_connected() :
                
                cursor = connection.cursor(dictionary=True)
                query = """select * from books limit 5 ;"""
                cursor.execute(query)
                results = cursor.fetchall()
                for row in results:
                    st.write(row)
                    book_id_list.append(row['book_id'])
            book_id = st.number_input('책 아이디 입력',min_value=book_id_list[0],max_value=book_id_list[-1])
            if st.button('실행'):
            
            
                if connection.is_connected() :
                    cursor = connection.cursor()

                    qurey = """delete from books 
                                where book_id = %s;"""
                    data = (book_id,)

                    cursor.execute(qurey,data)

                    connection.commit()

                
            
            
        except Error as e :
            print('디비 관련 에러 발생',e)
        
        finally :
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면 커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')

if __name__ == '__main__':
    main()