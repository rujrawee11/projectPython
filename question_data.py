import random #การสุ่มคำถาม

questions = [
    {
       "text": "ข้อใดคือผลลัพธ์ของการคำนวณต่อไปนี้ (8+3)*2-9/3 ?", # ข้อคำถาม1
        "bg": "Q1",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "33", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "19", "id": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "22", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "-11", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "จงตอบผลลัพธ์​ของ function ตามนี้ \nint(3), float(3.14), str('Hello')​", # ข้อคำถาม2
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "3, 3.14, Hello", "id": 1, "isAnswer": True }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "3, 3, 'Hello'", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "3, 3, Hello", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Errors", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "error ที่เกิดขึ้นจากการเขียน code \nผิดรูปแบบไวยากรณ์ของภาษานั้นๆ ?​", # ข้อคำถาม3
        "bg": "Q1",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "Syntax Errors", "id": 1, "isAnswer": True }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "Runtime Errors", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "Semantic  Errors", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Value Errors", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "error ใดๆ ก็ตามที่เกิดขึ้นระหว่าง run program อยู่ คือข้อใด ?", # ข้อคำถาม4
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "Semantic  Errors", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "Syntax Errors", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "Runtime Errors", "id": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Value Errors", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "กระบวนการในการปรับปรุงโปรแกรมที่ทำงานได้ถูกต้องอยู่แล้ว \nเพื่อเพิ่มคุณภาพของโปรแกรมให้ดีขึ้น เรียกว่าอะไร ?", # ข้อคำถาม5
        "bg": "Q1",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "Encapsulation", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "Generalization", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "Refactoring", "id": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Map", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": "ข้อใดคือคำตอบของผลลัพธ์​ function ดังต่อไปนี้ \nint('a'), str(1.0), int(100, 2), int('101', 2)", # ข้อคำถาม6
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "Error, 1.0, 100,\n 2 , Error", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "'a',​ 1, Error, Error", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "'a',​ '1.0'​, 100,\n2 , 5 ", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Error, '1.0',\n Error, 5", "id": 4, "isAnswer": True }
        ]
    },
    {
       "text": " คอมพิวเตอร์ใช้ภาษาระดับใด ?", # ข้อคำถาม7
        "bg": "Q1",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "python", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "machine", "id": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "high-level", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "natura", "id": 4, "isAnswer": False }
        ]
    },
    {
       "text": " x = "1"\ny = "2"\nprint(x+y)\nผลลัพธ์ตามโปรแกรมนี้คือข้อใด ?", # ข้อคำถาม8
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "x+y": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "1+2": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "12": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "3": 4, "isAnswer": False }
        ]
    },
    {
       "text": " set1 = {'tee', 'noey' ,'por', 'noyna'}\n          set2 = {'noey', 'sunthon', 'noyna', 'pop'}\nintersec = set1.intersection(set2)\nfor data in intersec:                           \nprint(data)                          ", # ข้อคำถาม9
        "bg": "Q1",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "tee         \nsunthon  y": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "sunthon  \nnoyna    ": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "noey       \nnoyna     ": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "por       \nnoey     ": 4, "isAnswer": False }
        ]
    },
    {
       "text": "word = "IT_KMITL"\nต้องprint()อย่างไรเพื่อที่จะแสดงผลลัพธ์ตัวสุดท้าย", # ข้อคำถาม10
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "word[-1]     ": 1, "isAnswer": True }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "word[6:8]    ": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "word[4:]      ": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "word[3:8]    ": 4, "isAnswer": False }
        ]
    },
    {
       "text": "ข้อใดเป็นตัวแปรชนิด list", # ข้อคำถาม11
        "bg": "Q1",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "a = {1, 2, 3, 4, 5}    ": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "a = (1, 2, 3, 4, 5)    ": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "a = <1, 2, 3, 4, 5> ": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "a = [1, 2, 3, 4, 5]    ": 4, "isAnswer": True }
        ]
    },
    {
       "text": "ข้อใดมีผลลัพธ์ False?  ", # ข้อคำถาม12
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "True and True or False and True       ": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "False and True or False and True      ": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "True or (8-5 == 3) and True or False": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "(2 >= 0) or (-5 <= -8)                         ": 4, "isAnswer": False }
        ]
    },
    {
       "text": "คำสั่งที่ใช้ในการให้เต่าเคลื่อนที่ไปข้างหน้าคือคำสั่งอะไร?", # ข้อคำถาม13
        "bg": "Q1",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "backward()": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "forward()": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "right()": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "left()": 4, "isAnswer": False }
        ]
    },
    {
        "text": "คำสั่งใดใช้รับข้อมูลทางแป้นพิมพ์?",  # ข้อคำถาม14
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "print()", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "compute()", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "output()", "id": 3, "isAnswer": False},
            {"text": "input()", "id": 4, "isAnswer": True}
        ]
    },
    {
        "text": "error ที่เกิดจากความผิดพลาดของ algorithm \nของผู้เขียนโปรแกรมคือข้อใด?",  # ข้อคำถาม15
        "bg": "Q1",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [
            # text คือ ตัวเลือกที่จะแสดงผล
            {"text": "Runtime Errors", "id": 1, "isAnswer": False},
            # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            {"text": "Syntax Errors", "id": 2, "isAnswer": False},
            # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            {"text": "Semantic  Errors", "id":