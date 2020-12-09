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
    }
]

def get_rand_question():
    return random.choice(questions)#random คำถาม