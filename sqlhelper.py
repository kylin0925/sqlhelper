#
#create table <name> (field1 type,field2 type,....)
#
#select * from <table> [where ...]
import sqlite3
class db:
    conn = None
    def db_connect(self,db_file):
        self.conn = sqlite3.connect(db_file)
    
    def db_sql(self,sql):
        c = self.conn.cursor()
        row = c.execute(sql)
        self.conn.commit()
        return row

    def db_close(self):
        self.conn.close()
def TEXTFIELD(s):
    return "'%s'" % (s)

class simpleDB(db):
    def set_db(self,db_file):
        self.db_connect(db_file)
    def create_table(self,table_name,field_content):
        sql = 'create table %s (%s)' % (table_name,field_content)
        r = self.db_sql(sql)
    def create_table_by_list(self,table_name,fields_list):
        lst = [" ".join(l) for l in fields_list]
        flatten = ",".join(lst)
        #print flatten 
        sql = 'create table %s (%s)' % (table_name,flatten)
        r = self.db_sql(sql)
    def query(self,table_name,fields,value): #all 
        sql = 'select * from %s where %s = %s ' % (table_name,fields,value) 
        r = self.db_sql(sql)
        res = r.fetchall()
        return res
    def add_item(self,table_name,field_list,value_list): # (f) values (v) 
        f = ",".join(field_list)
        v = ",".join(value_list)
        print f,v
        sql = 'insert into %s (%s) values (%s)' % (table_name,f,v)
        self.db_sql(sql)
    def update_item(self,table_name,field,value,cond):
        #update <table> set f=v,f2,=v2 where <cond>
        sql = "update %s set %s where %s"
        _s1_arr = zip(field,value) 
        _s2_arr = ["=".join(s) for s in _s1_arr ]
        _s3 = ",".join(_s2_arr)
        print _s2_arr,_s3 
        pass
    def delete_item(self,table_name,field,value):
        pass
#d =db()
#d.db_connect('test')
#r = d.db_sql('create table test (test Text)')
#r = d.db_sql('select * from sqlite_master')
#print r.fetchall()
#r = d.db_sql('insert into test (test) values (\'aaa\')')
#r = d.db_sql('select * from test')
#print r.fetchall()
#d.db_close()
_foo = simpleDB()
_foo.set_db('test3')
#_foo.create_table('wowo','test Text')
#_foo.create_table_by_list('test2',[['a','TEXT'],['b','TEXT']])
#print _foo.query('sqlite_master','name',TEXFIELD('wowo'))
#data = ['test',TEXTFIELD('aa')]
#_foo.add_item('wowo',['test'],[TEXTFIELD('aa')]);
f = ['a','b']
v = [TEXTFIELD('ABC'),TEXTFIELD('DEF')]
_foo.update_item('test',f,v,'a>1')
