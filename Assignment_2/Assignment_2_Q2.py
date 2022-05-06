#Taking input from User.
name = str(input("Name of Applicant: "))
'''I have used different data types here
        like int, str andfloat'''
SID = int(input("Enter your Student ID:"))

dep_name = str(input("Enter your department name: "))

cgpa = float(input("Enter your CGPA: "))

'''Here string is formed using multiline comment command which
gives us the string in the same body formate as we write inside this.'''

string= '''Hey, <name> Here!
My SID is <SID>
I am from <dep_name> department and my CGPA is <cgpa>'''

#As the string is replaced multiple times...we use this slicing in the given way.
print(string.replace("<name>", name).replace("<SID>", str(SID)).replace("<dep_name>", dep_name).replace("<cgpa>", str(cgpa)))
