def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    c = connection.cursor() 
    c.execute("PRAGMA foreign_keys=on;") 
    c.execute(sql_query) 
    connection.commit() 
    connection.close()

def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    c = connection.cursor() 
    c.execute(sql_query) 
    ans= c.fetchall()  
    connection.close()
    return ans


class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass
	
class Student:
    def __init__(self, student_id = None ,name = None, age = None , score = None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score = score

    
    def __repr__(self):
        return str("Student(student_id={0}, name={1}, age={2}, score={3})".format
        (self.student_id,
        self.name,
        self.age,
        self.score))
    
    
    
    @classmethod
    def get (cls,**kwargs):
        for k,v in kwargs.items():
            #print(k,v)
            
            if 'score' == k:
        
                data = read_data('''select * from Student where score = {}'''.format(v))
            
            
            elif 'name' == k:

                data = read_data('''select * from Student where name like "%{}%"'''.format(v))
                
            elif 'age' == k:
            
                data = read_data('''select * from Student where age = {}'''.format(v))
                
                
            elif 'student_id' == k:
            
                data = read_data('''select * from Student where student_id = {}'''.format(v))
              
                
            else:
                raise InvalidField
                
            if len(data) > 1:
                raise MultipleObjectsReturned
                
            elif len(data) == 0:
                raise DoesNotExist
                
            else:
                return Student(*data[0])    
                            
            
    def delete(self):
        write_data(''' delete  from Student where student_id = {}'''.format(self.student_id))
        
    def save(self):
        print(self.name,self.age,self.score)def write_data(sql_query):
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
        
    def __repr__(self):
    
            return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
                self.student_id,
                self.name,
                self.age,
                self.score)
        
        
    
    
    
    
    @classmethod    
    def get(cls,**kwargs):
        
        for k,v in kwargs.items():
            
            if 'score'== k :
                data = read_data('''select * from student where score = {}''' . format(v))
            
            elif 'name' == k :
                data = read_data('''select * from student where name like '%{}%' ''' . format(v))
                
            elif 'age'== k :
                data = read_data('''select * from student where age = {}''' . format(v))
            
            elif 'student_id' == k :
                data = read_data('''select * from student where student_id = {}''' . format(v))
                
            
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
        for k,v in kwargs.items():
            key = (k.split('__'))
            value = v
            
            if len(key) == 1:
                if key[0] in ['student_id','age','score']:
                    data = read_data('''select * from Student where {} = {}'''.format(key[0],v))
                    
                elif key[0] == 'name':
                    data = read_data('''select * from Student where {} like '%{}%' '''.format(key[0],v))
                    
            
            elif(len(key) > 1):        
                
                if key[1] == 'lt':
                    if key[0] in ['age','score','student_id']:
                        data = read_data('''select * from Student where {} < {}'''.format(key[0],v))
                        
                    
                elif key[1] == 'gt':
                    if key[0] in ['age','score','student_id']:
                        data = read_data('''select * from Student where {} > {}'''.format(key[0],v))
                        
                elif key[1] == 'lte':
                    if key[0] in ['age','score','student_id']:
                        data = read_data('''select * from Student where {} <= {}'''.format(key[0],v))
                        
                elif key[1] == 'gte':
                    if key[0] in ['age','score','student_id']:
                        data = read_data('''select * from Student where {} >= {}'''.format(key[0],v))
                        
                elif key[1] == 'in':
                    if key[0] in ['name','age','score','student_id']:
                        data = read_data('''select * from Student where {} in {}'''.format(key[0],tuple(v)))
                        
                    
                elif key[1] == 'neq':
                    if key[0] in ['age','score','student_id']:
                        data = read_data('''select * from Student where {} <> {}'''.format(key[0],v))
                        
                    elif key[0] == 'name':
                        data = read_data('''select * from Student where {} <> '{}' '''.format(key[0],v))
                        
                elif key[1] == 'contains' :
                    if key[0] == 'name':
                        data = read_data('''select * from Student where {} like '%{}%' '''.format(key[0],v))
                        
                        
                        
            lis = []
            print(len(data))
            if len(data) != 0:
                for row in range(len(data)):
                    lis.append(Student(*data[row]))
            else:
                return []
                            
        return lis
                    
                        
                
                    
                
                
                    
                
                    
           
            
            
                
            
        
        
            
'''        
selected_students = Student.filter(age__neq=34)
print(selected_students)'''
'''
selected_students = Student.filter(age=23)
print(selected_students)
print(Student.filter(age=100))'''




        import sqlite3
        connection = sqlite3.connect("selected_students.sqlite3")
        c = connection.cursor()
        
        if self.student_id == None:
            c.execute('''insert into Student (name,age,score) values (?,?,?)''',(self.name,self.age,self.score))
            self.student_id = c.lastrowid
        
        
        elif self.name != None:
            c.execute('''insert or REPLACE into  Student (student_id,name,age,score) values (?,?,?,?)''',(self.student_id,self.name,self.age,self.score))
            self.student_id = c.lastrowid
            
        else:
            c.execute('''update Student set name = ?,age = ?,score = ? where student_id = ?''',(self.name,self.age,self.score,self.student_id))
        
        connection.commit()
        connection.close()
        
    
    
    
    @classmethod
    def filter(cls,**kwargs):
        keys = [];val = []
        for k,v in kwargs.items():
            
            key = (k.split('__'))
            value = v
            
            if len(key) ==1:
                if key[0] in ['age','score','student_id']:
                    data = read_data('''select * from Student where {} = {}'''.format(key[0],v))
                    if len(data) != 0:
                        return(Student(*data[0]))
                    else:
                        return []
                    
                elif key[0] == 'name':
                    data = read_data('''select * from Student where {} like "%{}%" '''.format(key[0],v))
                    if len(data) != 0:
                        return(Student(*data[0]))
                    else:
                        return []
                    
                else:
                    raise InvalidField
                    
            if len(key) > 1:
                
                if key[1] == 'lt':
                    if key[0] in ['age','score','student_id']:
                        data = read_data('''select * from Student where {} < {}'''.format(key[0],v))
                        #print(len(data))
                        lis = []
                        if len(data) != 0:
                            for row in range(len(data)):
                                lis.append(Student(*data[row]))
                        else:
                            return []
                        
                    return lis
                    
                    
                    
                
                
'''
selected_students = Student.filter(age__lt = 35)
print(selected_students)        

selected_students = Student.filter(age=34,name = )
print(selected_students)

selected_students = Student.filter(age = 34,name = 'Jesse Couch')
print(selected_students)
'''
