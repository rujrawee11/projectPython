import random #การสุ่มคำถาม

questions = [
    {
       "text": "ข้อใดคือผลลัพธ์ของการคำนวณต่อไปนี้ (8+3)*2-9/3 ?", # ข้อคำถาม
        "bg": "Q2",  # รูปภาพพื้นหลัง ตอนนี้มีแค่ Q1 และ Q2
        "choices": [ 
            { "text": "19", "id": 1, "isAnswer": True }, # text คือ ตัวเลือกที่จะแสดงผล
            { "text": "33", "id": 2, "isAnswer": False },  # id ให้เป็นเลขที่ไม่ซ้ำกัน เพื่อระบุตัวเลือก แนะนำ 1,2,3,4
            { "text": "22", "id": 3, "isAnswer": False }, # isAnswer คือ ตัวเลือกนี้เป็นคำตอบที่ถูกหรือไม่ True คือ คำตอบที่ถูกต้อง ส่วน False เป็นคำตอบที่ผิด
            { "text": "-11", "id": 4, "isAnswer": False } 
        ]
    },
    {
        "text": "2 a + b = ?", 
        "bg": "Q2", 
        "choices": [ 
            { "text": "19 T", "id": 1, "isAnswer": True }, 
            { "text": "33", "id": 2, "isAnswer": False }, 
            { "text": "22", "id": 3, "isAnswer": False }, 
            { "text": "-11", "id": 4, "isAnswer": False } 
        ]
    },
    {
        "text": "ข้อใดต่อไปนี้เป็น keyword ในภาษา Python 3 ทั้งหมด?", 
        "bg": "Q1", 
        "choices": [ 
            { "text": "class, do, try", "id": 1, "isAnswer": False }, 
            { "text": "with, where, is", "id": 2, "isAnswer": False }, 
            { "text": "final, pass, assert", "id": 3, "isAnswer": False }, 
            { "text": "assert, from, pass", "id": 4, "isAnswer": True } 
        ]
    }
]

def get_rand_question():
    return random.choice(questions)