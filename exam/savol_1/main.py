from task import send_sms

tasks = [send_sms]
for i in tasks:
    send_sms().delay()

"""
Celery - bu Python-da yozilgan ochiq manbali taqsimlangan vazifalar navbati tizimi.
U bir nechta ishchi jarayonlar yoki mashinalar bo'ylab vazifalarni (ko'pincha 
ko'p vaqt talab qiladigan yoki resurslarni talab qiladigan) boshqarish va taqsimlashda
yordam berish uchun mo'ljallangan.
"""
# shu usulda run beriladi
# celery -A main.py worker --loglevel=info
