def hello():
    print('Hello my friend')

def sawatdee():
    print('สวัสดี')

def nihao():
    print('หนีห่าว')

def konichiwa():
    print('คนนิจิวะ')
    
while True:
    friend = input('Where are you from?: ')

    if friend == 'thai':
        sawatdee()
    elif friend == 'china':
        nihao()
    elif friend == 'japanese':
        konichiwa()
    else:
        hello()
