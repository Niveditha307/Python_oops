def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans


class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass



class Student:
    def __init__(self, student_id = None,name = None, age = None, score = None):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.score = score
        self.val = None
        
    def __repr__(self):
    
            return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
                self.student_id,
                self.name,
                self.age,
                self.score)
        
        
    
    
    
    
    @classmethod    
    def get(cls,**kwargs):
        
        for k,v in kwargs.items():
            
            attr = ['name','score','age','student_id']
            
            if k in attr:
                data = read_data('''select * from student where {} = '{}' ''' . format(k,v))
            
            else : 
                raise InvalidField
                
            
                
            if len(data) > 1:
                raise MultipleObjectsReturned
                
            elif len(data) == 0:
                raise DoesNotExist
            
            else :
                obj = Student(*data[0])
                return (obj)
                
                
                
    def delete(self):
        write_data('''delete from student where student_id = {}'''.format(self.student_id))
         
         
    def save(self):
        
            import sqlite3
            conn = sqlite3.connect("selected_students.sqlite3")
            c = conn.cursor()
            if(self.student_id == None):
                c.execute('''insert into student(name,age,score) values (?,?,?)''',(self.name,self.age,self.score))
                self.student_id = c.lastrowid
            else :
               c.execute('''insert or REPLACE into student(student_id,name,age,score) values (?,?,?,?)''',(self.student_id ,self.name,self.age,self.score))       
            conn.commit()
            conn.close()
            
            
    @classmethod
    def filter(cls,**kwargs):
        #global val
        list = ['age','name','score','student_id']
        multiple_values = []
        
        for k,v in kwargs.items():
            key = k.split('__')
            oper = {'gt':'>', 'lt':'<', 'lte':'<=', 'gte':'>=', 'neq':'<>', 'eq' : '='}
            
            if key[0] not in list:
                raise InvalidField
                
            elif len(key) == 1:
                val = "{} {} '{}'".format(key[0],oper['eq'],v)
                
            
            elif key[1] == 'in':
                v =tuple(v)
                val = "{} {}  {} ".format(key[0],'IN',v)
                
            elif key[1] == 'contains' :
                val = "{} {} '%{}%' ".format(key[0],'LIKE',v)
            
            else :
                val = "{} {} '{}'".format(key[0],oper[key[1]],v)
                
            multiple_values.append(val)
            
        x = ' AND '.join(multiple_values)
        
        data = read_data("select * from student where {}".format(x))
        
        li = []
        
        if(len(data)!=0):
            for i in range(len(data)):
                li.append(Student(*data[i]))
            return li
        else :
            return []
        

'''
selected_students = Student.filter(age__lte=30)
print(selected_students)

print(Student.filter(age=100))

selected_students = Student.filter(age__in = [25, 34], score__lt=50)
print(selected_students)'''
