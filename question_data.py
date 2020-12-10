import random #การสุ่มคำถาม

questions = [
    {
       "text": "ข้อใดคือผลลัพธ์ของการคำนวณต่อไปนี้ (8+3)*2-9/3 ?", # ข้อคำถาม1
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "33", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "19", "id": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "22", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "-11", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "จงตอบผลลัพธ์​ของ function ตามนี้ \nint(3), float(3.14), str('Hello')​", # ข้อคำถาม2
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "3, 3.14, Hello", "id": 1, "isAnswer": True }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "3, 3, 'Hello'", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "3, 3, Hello", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Errors", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "error ที่เกิดขึ้นจากการเขียน code \nผิดรูปแบบไวยากรณ์ของภาษานั้นๆ ?​", # ข้อคำถาม3
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "Syntax Errors", "id": 1, "isAnswer": True }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "Runtime Errors", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "Semantic  Errors", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Value Errors", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "error ใดๆ ก็ตามที่เกิดขึ้นระหว่าง run program อยู่ คือข้อใด ?", # ข้อคำถาม4
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "Semantic Errors", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "Syntax Errors", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "Runtime Errors", "id": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Value Errors", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "กระบวนการในการปรับปรุงโปรแกรมที่ทำงานได้ถูกต้องอยู่แล้ว\nเพื่อเพิ่มคุณภาพของโปรแกรมให้ดีขึ้น เรียกว่าอะไร ?", # ข้อคำถาม5
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "Encapsulation", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "Generalization", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "Refactoring", "id": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Map", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "ข้อใดคือคำตอบของผลลัพธ์​ function ดังต่อไปนี้\nint('a'), str(1.0), int(100, 2), int('101', 2)", # ข้อคำถาม6
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "Error, 1.0, 100,\n2 , Error", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "'a',​ 1, Error, Error", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "'a',​ '1.0'​, 100,\n2 , 5 ", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Error, '1.0',\n Error, 5", "id": 4, "isAnswer": True }
        ]
    },
    {
       "text": "คอมพิวเตอร์ใช้ภาษาระดับใด ?", # ข้อคำถาม7
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "python", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "machine", "id": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "high-level", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "natura", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "x = 1\ny = 2\nprint(x+y)\nผลลัพธ์ตามโปรแกรมนี้คือข้อใด ?", # ข้อคำถาม8
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "x+y", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "1+2", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "12", "id": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "3", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "set1 = {'tee', 'neay' ,'por', 'noyna'}\nset2 = {'neay', 'sunthon', 'noyna', 'pop'}\nintersec = set1.intersection(set2)\nfor data in intersec:\nprint(data)", # ข้อคำถาม9
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "tee\nsunthon", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "sunthon\nnoyna", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "neay\nnoyna", "id": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "por\nneay", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "word = IT_KMITL\nต้องprint()อย่างไรเพื่อที่จะแสดงผลลัพธ์ตัวสุดท้าย", # ข้อคำถาม10
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "word[-1]", "id": 1, "isAnswer": True }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "word[6:8]", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "word[4:]", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "word[3:8]", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "ข้อใดเป็นตัวแปรชนิด list", # ข้อคำถาม11
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "a = {1, 2, 3, 4, 5}", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "a = (1, 2, 3, 4, 5)", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "a = <1, 2, 3, 4, 5>", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "a = [1, 2, 3, 4, 5]", "id": 4, "isAnswer": True }
        ]
    },
    {
       "text": "ข้อใดมีผลลัพธ์ False ?", # ข้อคำถาม12
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "True and True or \nFalse and True", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "False and True or \nFalse and True", "id": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "True or (8-5 == 3) \nand True or False", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "(2 >= 0) or\n (-5 <= -8)     ", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "คำสั่งที่ใช้ในการให้เต่าเคลื่อนที่ไปข้างหน้าคือคำสั่งอะไร ?", # ข้อคำถาม13
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [ 
            { "text": "backward()", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "forward()", "id": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "right()", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "left()", "id": 4, "isAnswer": False }
        ]
    },
    {
        "text": "คำสั่งใดใช้รับข้อมูลทางแป้นพิมพ์ ?",  # ข้อคำถาม14
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "print()", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "computer()", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "output()", "id": 3, "isAnswer": False},
            {"text": "input()", "id": 4, "isAnswer": True}
        ]
    },
    {
        "text": "error ที่เกิดจากความผิดพลาดของ algorithm \nของผู้เขียนโปรแกรมคือข้อใด ?",  # ข้อคำถาม15
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "Runtime Errors", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "Syntax Errors", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "Semantic  Errors", "id": 3, "isAnswer": True},
            {"text": "Value  Errors", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "ข้อใดต่อไปนี้เป็น keyword ในภาษา Python 3 ทั้งหมด ?",  # ข้อคำถาม16
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "class, do, try", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "with, where, is", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "final, pass, assert", "id": 3, "isAnswer": False},
            {"text": "assert, from, pass", "id": 4, "isAnswer": True}
        ]
    },
    {
        "text": "ข้อใดคือผลลัพธ์ของ 2** 3 ** 2 // 10 + 123 % 2 ?",  # ข้อคำถาม17
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "7.4", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "52", "id": 2, "isAnswer": True},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "52.2", "id": 3, "isAnswer": False},
            {"text": "7", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "ประเภทของข้อมูลใดที่เราควรใช้\nเพื่อจัดเก็บข้อมูลของจำนวนนักศึกษาในคลาสเรียน ?",  # ข้อคำถาม18
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "int", "id": 1, "isAnswer": True},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "bool", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "float", "id": 3, "isAnswer": False},
            {"text": "string", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "ข้อใดแสดงผลลัพธ์ Error ?",  # ข้อคำถาม19
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "float('12'*3)", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "float('12'+'3')", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "float('12+3')", "id": 3, "isAnswer": True},
            {"text": "float('1'*2+'3')", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "text = [banana, apple, [grape, watermelon]]\nprint(len(text))\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม20
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "3", "id": 1, "isAnswer": True},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "4", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "5", "id": 3, "isAnswer": False},
            {"text": "6", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "text = ['pink', 'red', ['green', 'orange'], 'blue']\nprint((text[2][1]))\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม21
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "green", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "blue", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "orange", "id": 3, "isAnswer": True},
            {"text": "blue", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "text = 'bAnAnA'\ntext = text.swapcase()\nprint(text)\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม22
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "bAnAnA", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "banana", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "BaNAnA", "id": 3, "isAnswer": False},
            {"text": "BaNaNa", "id": 4, "isAnswer": True}
        ]
    },
    {
        "text": "number = [3, 5, 7, 1, 2] \nnumber.sort()\nprint(*number)\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม23
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "3 5 7 1 2", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "1 2 3 5 7", "id": 2, "isAnswer": True},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "7 5 3 2 1", "id": 3, "isAnswer": False},
            {"text": "1 2 3 7 5", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "name = set(['I', 'T', 'K', 'M', 'I', 'T', 'L'])\nprint(name)\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม24
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "'M', 'L', 'K', 'T', 'I'", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "M, L, K, T, I", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "{'M', 'L', 'K', 'T', 'I'}", "id": 3, "isAnswer": True},
            {"text": "[{'M', 'L', 'K', 'T', 'I'}]", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "num = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}\nprint(num)\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม25
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "{1}", "id": 1, "isAnswer": True},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "1, 1, 1, 1, 1, 1, 1, 1, 1, 1", "id": 3, "isAnswer": False},
            {"text": "1", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "all_num = {[1, 2, 3], [4, 5, 6]}\nprint(all_num)\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม26
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "{[1, 2, 3], [4, 5, 6]}", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "[1, 2, 3], [4, 5, 6]", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "1, 2, 3, 4, 5, 6", "id": 3, "isAnswer": False},
            {"text": "Error", "id": 4, "isAnswer": True}
        ]
    },
    {
        "text": "name = set(['tee', 'noey', 'por', 'sunthorn'])\nname.discard('noey')\nname.discard('sunthorn')\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม27
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "'tee', 'por'", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "{'tee', 'por'}", "id": 2, "isAnswer": True},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "tee, por", "id": 3, "isAnswer": False},
            {"text": "{'tee', 'por'}", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "usernames = ['Winwin', 'Kun', 'Lucus']\nallist = [1, 3.14, 'itkmitl', True, [5, 10, 'Hello']]\nuser_count = len(usernames)\nalist_size = len(allist)\nprint(user_count)\nprint(alist_size)\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม28
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "3\n5", "id": 1, "isAnswer": True},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "3\n7", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "1\n2", "id": 3, "isAnswer": False},
            {"text": "1\n1", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "text = ['a', 'b', 'c', 'd']\nprint(text.index('c'))\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม29
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "0", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "1", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "2", "id": 3, "isAnswer": True},
            {"text": "3", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "text = ['a', 'b', 'c', 'd']\nprint(text.index('c'))\nได้ผลลัพธ์ตามข้อใด ?",  # ข้อคำถาม30
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "0", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "1", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "2", "id": 3, "isAnswer": True},
            {"text": "3", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "ข้อใดคือคำที่ห้ามนำมาตั้งเป็นชื่อตัวเเปร ?",  # ข้อคำถาม31
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "low", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "height", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "elif", "id": 3, "isAnswer": True},
            {"text": "banana", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "ข้อใดคือตัวดำเนินการที่หมายถึงการยกกำลังในภาษา python ?",  # ข้อคำถาม32
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "*", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "**", "id": 2, "isAnswer": True},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "***", "id": 3, "isAnswer": False},
            {"text": "^", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "import ____ as pd \nควรเติมคำในข้อใดในช่องว่าง ?",  # ข้อคำถาม33
        "bg": "Q2",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "numpy", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "pandas", "id": 2, "isAnswer": True},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "math", "id": 3, "isAnswer": False},
            {"text": "python", "id": 4, "isAnswer": False}
        ]
    },
    {
        "text": "import ____ as np \nควรเติมคำในข้อใดในช่องว่าง ?",  # ข้อคำถาม34
        "bg": "Q1",  # รูปภาพพื้นหลัง
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "numpy", "id": 1, "isAnswer": True},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "pandas", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "math", "id": 3, "isAnswer": False},
            {"text": "python", "id": 4, "isAnswer": False}
        ]
    }
]

def get_rand_question():
    return random.choice(questions)#random คำถาม