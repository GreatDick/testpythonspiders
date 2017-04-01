import random
#import pymysql
sa=''
seed='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-'
salt=random.sample(seed,8)
print(''.join(salt))
input()
# def storeInMysql(codelist):
     # try:
	     # conn=pymysql.connect(host='139.224.13.102',user='root',passwd='wangli2014',db='mysql')
		 # cur=conn.cursor()
	 # except BaseException as e:
	     # print(e)
	 # else:
	     # try:
		       # cur.execute('CREATE DATABASE ID NOT EXITS code')
			   # cur.execute('USE activation_code')
			   # cur.execute('''CREATE TABLE IF NOT EXISTS code(
                            # id INT NOT NULL AUTO_INCREMENT,
                            # code VARCHAR(32) NOT NULL,
                            # PRIMARY KEY(id)
                        # )''')
			    # cur.execute('INSERT INTO code(code) VALUES(%s)',(salt))
				# cur.connection.commit()
        # except BaseException as e:
            # print(e)
    # finally:
        # cur.close()
        # conn.close()
# if __name__ == '__main__':
    # storeInMysql(generateActivationCode(200))
    # print('OK!')