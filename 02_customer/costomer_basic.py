import re, pickle, json
# custlist=[
#    {'name': '홍길동', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthyear': '2000'},
#    {'name': '김철수', 'gender': 'M', 'email': 'kim010@gmail.com', 'birthyear': '2001'},
#    {'name': '박나리', 'gender': 'F', 'email': 'park1@gmail.com', 'birthyear': '2002'},
#]
#page=2

# f = open('02_customer/data.pickle', 'rb')
# custlist = pickle.load(f)
# page = len(custlist)-1

f = open('02_customer/data.json', 'r')
custlist = json.load(f)
page = len(custlist)-1

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()

    if choice=="I":        
        print("고객 정보 입력")
        customer = {'name':'','gender':'','email':'','birthyear':''}
        customer['name'] = input('이름을 입력하세요 >>>')
        while True:
            customer['gender'] = input('성별을 입력하세요(M,F) >>>').upper()
            if customer['gender'] in ('M', 'F'):
                break
        while True:
            regex = re.compile('^[a-z][a-z0-9]{4,20}@[a-z]{2,10}[.][a-z]{2,10}') #대괄호 바깥쪽의 ^는 시작을 의미. 안쪽의 ^는 부정의 의미. '.'는 [.]로 써야함.
            while True:
                customer['email'] = input('이메일을 입력하세요 >>>')
                check = regex.search(customer['email'])
                if check:
                    break
                else:
                    print('@를 포함한 정확한 이메일을 입력하세요')
            id_check = 0
            for i in custlist:
                if i['email'] == customer['email']:
                    id_check = 1
                    break
            if id_check == 0:
                break
            print('중복되는 이메일이 있습니다.')
        while True:
            customer['birthyear'] = input('출생년도 4자리로 입력해 주세요 >>>')
            if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
                break
        print(customer)
        custlist.append(customer)
        print(custlist)
        page = len(custlist)-1
        print(page)

    elif choice=="C":
        print("현재 고객 정보 조회")
        if page >= 0:
            print(f'현재 페이지는 {page+1}쪽입니다.')
            print(custlist[page])
        else:
            print('입력된 정보가 없습니다.')

    elif choice == 'P':
        print("이전 고객 정보 조회")
        if page <= 0:
            print('첫번째 페이지입니다.')
            print(page)
        else:
            page -= 1
            print(f'현재 페이지는 {page+1}쪽입니다.')
            print(custlist[page])

    elif choice == 'N':
        print("다음 고객 정보 조회")
        if page >= len(custlist)-1:
            print('마지막 페이지입니다.')
            print(page)
        else:
            page += 1
            print(f'현재 페이지는 {page+1}쪽입니다.')
            print(custlist[page])

    elif choice=='D':
        print("고객 정보 삭제")
        choicel = input('삭제하려는 이메일을 입력하세요 >>>')
        delok = 0
#        for i in range(0,len(custlist)):
#            print(custlist[i])
        for i,item in enumerate(custlist):
            if item['email'] == choicel:
                name = custlist.pop(i)['name']
                print(f'{name}고객님의 정보가 삭제되었습니다.')   
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
            print(custlist)
        if page >= len(custlist):
            page = len(custlist)-1
        print(f'현재 페이지는 {page+1}쪽입니다.')

    elif choice=="U": 
        print("고객 정보 수정")
        while True:
            choicel = input('수정하려는 이메일을 입력하세요 >>>')
            idx = -1
            for i in range(0, len(custlist)):
                if custlist[i]['email'] == choicel:
                    idx = i
                    break
            if idx == -1:
                print('등록되지 않은 이메일입니다.')
                break
            choice2 = input('''
다음 중 수정할 항목을 입력하세요.
(name,gender,birthyear)
수정할 정보가 없으면 "exit" 
>>> ''')
            if choice2 in ('name', 'gender', 'birthyear'):
                custlist[idx][choice2] = input(f'수정할 {choice2}를 입력하세요 >>> ')
                break
            elif choice2 == 'exit':
                break
            else:
                print("존재하지 않는 정보입니다.")
                break
            
    elif choice=="Q":
        print("프로그램 종료")
#        f = open("02_customer/data.pickle", "wb") #바이너리 형태이기에 w뒤에 b를 붙임. +경로 지정
#        pickle.dump(custlist,f)       #파일로 안되어있는건 s, 파일로 바로 나갈거니 s 안 붙이기
#        f.close()
        
        f = open("02_customer/data.json", "w")
        json.dump(custlist,f,indent=2)
        f.close()
        break
