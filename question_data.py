import random #การสุ่มคำถาม

questions = [
    {
       "text": "ข้อใดคือผลลัพธ์ของการคำนวณต่อไปนี้ (8+3)*2-9/3 ?", # ข้อคำถาม
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "33", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "19", "id": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "22", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "-11", "id": 4, "isAnswer": False } 
        ]
    },
    {
       "text": "จงตอบผลลัพธ์​ของ function ตามนี้ \nint(3), float(3.14), str('Hello')​", # ข้อคำถาม
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "3, 3.14, Hello", "id": 1, "isAnswer": True }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "3, 3, 'Hello'", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "3, 3, Hello", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Errors", "id": 4, "isAnswer": False } 
        ]
    },
    {
       "text": "error ที่เกิดขึ้นจากการเขียน code \nผิดรูปแบบไวยากรณ์ของภาษานั้นๆ ?​", # ข้อคำถาม
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "Syntax Errors", "id": 1, "isAnswer": True }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "Runtime Errors", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "Semantic  Errors", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Value Errors", "id": 4, "isAnswer": False } 
        ]
    },
    {
       "text": "error ใดๆ ก็ตามที่เกิดขึ้นระหว่าง run program อยู่ คือข้อใด ?", # ข้อคำถาม
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "Semantic  Errors", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "Syntax Errors", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "Runtime Errors", "id": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Value Errors", "id": 4, "isAnswer": False } 
        ]
    },
    {
       "text": "กระบวนการในการปรับปรุงโปรแกรมที่ทำงานได้ถูกต้องอยู่แล้ว \nเพื่อเพิ่มคุณภาพของโปรแกรมให้ดีขึ้น เรียกว่าอะไร ?", # ข้อคำถาม
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "Encapsulation", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "Generalization", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "Refactoring", "id": 3, "isAnswer": True }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Map", "id": 4, "isAnswer": False } 
        ]
    },
    {
       "text": "ข้อใดคือคำตอบของผลลัพธ์​ function ดังต่อไปนี้ \nint('a'), str(1.0), int(100, 2), int('101', 2)", # ข้อคำถาม
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "Error, 1.0, 100,\n 2 , Error", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "'a',​ 1, Error, Error", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "'a',​ '1.0'​, 100,\n2 , 5 ", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "Error, '1.0',\n Error, 5", "id": 4, "isAnswer": True } 
        ]
    },
        {
       "text": " คอมพิวเตอร์ใช้ภาษาระดับใด ?", # ข้อคำถาม
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "python", "id": 1, "isAnswer": False }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "machine", "id": 2, "isAnswer": True },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "high-level", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "natura", "id": 4, "isAnswer": False } 
        ]
    },



]

def get_rand_question():
    return random.choice(questions)