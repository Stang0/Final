
#function ที่ใช้ เช็คว่าพวกชื่อ พวก id มันซ่ำหรือมันควรจะเป็นชื่อคนไหม 
def Validation_Name_and_LastName(AllStudentData):
    CheckValidation = ['1','2','3','4','5','6','7','8','9','0']
    StudentID = input("ใส่เลขID")
    for i in AllStudentData:
        if StudentID == i['id']:
            print('รหัสนักศึกษาซ้ำ')
            Select_Option(AllStudentData)
    if len(StudentID) == 0:
        print("โปรดใส่ID")
        Select_Option(AllStudentData)
    for i in StudentID:
        if i not in CheckValidation:
            print('ใส่ได้แค่ตัวเลข')
            Select_Option(AllStudentData) 
    StudentName = input('ใส่ขื้่อ')
    if len(StudentName) == 0:
        print("โปรดใส่ชื่อ")
        Select_Option(AllStudentData)
    for i in StudentName:
        if i in CheckValidation:
            print('กรุณาใส่ชื่อให้ถูกต้อง')
            Select_Option(AllStudentData)
    StudentLastName = input('ใส่นามสกุล')
    if len(StudentLastName) == 0:
        print("โปรดใส่นามสกุล")
        Select_Option(AllStudentData)
    for i in StudentLastName:
        if i in CheckValidation:
            print('กรุณาใส่นามสกุณให้ถูก')
            Select_Option(AllStudentData)
    return StudentID,StudentName,StudentLastName


# เก็บข้อมูลนักศึกษาทีกรอก ลงตัวแปรชั่วคราว แล้ว return ออกไปใช้ที่ Select_Option
def AddStudentToDict(StudentID:int,StudentName:str,StudentLastName:str):
    StudentData = {'id':StudentID,"name":StudentName,"lastName":StudentLastName}
    return StudentData


# เป็น function ที่ใช่เพื่อชื่อ นศ ลงตัวแปรชั่วคราว
def AddStudent(StudentID:int,StudentName:str,StudentLastName:str):
    StudentData = AddStudentToDict(StudentID , StudentName , StudentLastName)
    return  StudentData

# แสดงชื่อ นศ 
def ShowStudent(AllStudentData):
    print('แสดงชื่อนักศึกษาแบบ Dist')
    for i in AllStudentData:
        print('ID:',i['id'],"Name:",i['name'],"LastName",i['lastName'])


#เรียกใช้ function Validation_Name_and_LastName และส่งAllStudentData เพื่อไปเช็คว่า ID ที่กำลัง Add ไปใหม่มันตรงกับที่มีอยู่แล้วรึป่าว  เพื่อเช็คให้ถูกว่า ชื่อก็ไ่มควรเป็นตัวเลข อะไรประมาณนั้น
def read_one_student(AllStudentData):
    StudentID,StudentName,StudentLastName = Validation_Name_and_LastName(AllStudentData)
    return StudentID,StudentName,StudentLastName

#รับ id ที่อยากจะเรียกดูข้อมูล จากนั้น loop ข้อมูลที่เก็บทั้งหมดจาก AllStudentData
#โดย ถ้า StudentID ที่กรอกตรงกับ ข้อมูลของ id ที่เรา loop อันไหนเราก็จะดึงข้อมูลนั้นมาแสดง
def Get_Student_Data(AllStudentData):
    StudentID = input("กรุณาใส่รหัสนักศึกษาที่ต้องการค้นหา: ")
    for i in AllStudentData:
        if StudentID == i['id'] :
            for k,v in i.items():
                print(f"ข้อมูลที่ค้นพบ: {k,v}")
    print('ไม่พบข้อมูลที่ตรงกับรหัสนักศึกษา')

def Create_LogFile(AllStudentData):
    with open('Data.txt', 'a') as file:
        for i in AllStudentData:
            file.write('\n------------------------')
            for k,v in i.items():
                Content = f'\n{k}:{v}'
                file.write(Content)

#function Select_Option เป็น function ที่ให้ user เลือกว่าจะทำอะไรกับหัวข้อที่มีมาให้

#ถ้า User input 1 เข้ามาก็คือเพิ่มข้อมูลนักศึกษา โดยไปเรียกใช้ function read_one_student โดยจะส่งAllStudentData เข้าไปด้วยเพื่อเช็คว่า ID ที่ user จะเพิ่มมันมีอยู่แล้วในตัวแปรที่เราเก็บข้อมูลไหม ก่อนเพื่อรับข้อมูลที่User inputเข้ามาโดยจะ return ออกมาเป็น StudentID , StudentName , StudentLastName 
#หลังจากที่ทำในส่วนของ read_one_student เสร็จ จะเรียกใช้ AddStudent โดยส่ง StudentID , StudentName , StudentLastName เข้าไปทำงานเพื่อนำลงไปเก็บไว้ บนตัวแปรชั่วคราว ก่อนนำลงไปเก็บ ลงตัวแปล (AllStudentData) ที่เก็บข้อมูลนศ ทั้งหมด
#โดย AddStudent จะ return StudentData

#ถ้า User input 2 เข้ามาก็คือจะเป็นการเรียกดูข้อมูล 
#จะเรียกใช้ function Get_Student_Data โดยส่ง Allstudentเข้าไป    เพราะว่าเราจะเรียกดูข้อมูลเราต้องส่งตัวแปรท่ี่เก็บข้อมูลไปด้วย เพื่อใช้ID ในการเช็คว่าจะเรียกดู ข้อมูลของคนไหน

#ถ้า User input 3 ก็คือหยุดทำงาน แต่ก่อนหยุดทำงานก็จะให้ show นศ ทั้งหมดก่อนโดยเรียกใช้ function ShowStudent โดยส่ง (AllStudentData) เข้าไปทำงานน 

#ถ้า User input 4 ก็คือ สร้างLogFile โดยเรียกใช้ฟังชั่นCreate_Logfile

def Select_Option(AllStudentData):
    while True:
        Add = input('1)ต้องการเพิ่มข้อมูลนักศึกษา\U0001f600 \n''2)ต้องการเรียกดูข้อมูลนักศึกษา \U0001F606 \n''3)หยุดการทำงาน\U0001F923\n' '4.สร้างLogFile\n'    '--->')
        if Add == '1': 
            StudentID , StudentName , StudentLastName = read_one_student(AllStudentData)
            StudentData = AddStudent(StudentID , StudentName , StudentLastName)
            AllStudentData.append(StudentData)
        elif Add == '2':
            Get_Student_Data(AllStudentData)
        elif Add == '3':
            ShowStudent(AllStudentData)
            exit()
        elif Add == '4':
            Create_LogFile(AllStudentData)
        else:
            print("โปรดเลือกเลขตามหัวข้อ")

#ในmain() จะเก็บ AllStudentData ที่เก็บข้อมูลแบบ Array [] แล้วแต่ละ object{}  ก็จะเก็บมาลงใน array AllStudentData [{"id":"....","name","....","lastname","....."},{},{} ] การเก็บข้อมูลของ AllStudentData จะเป็นประมาณนี้
#พอสร้าง ตัวแปรไว้เก็บข้อมูลแล้วก็จะไปเรียกใช้ function Select_Optionและส่ง AllStudentData  เข้าไปทำงาน

def main():
    AllStudentData = []
    Select_Option(AllStudentData)

#เริ่มเรียกใช้งาน function main() 
if __name__ == '__main__':
    main()