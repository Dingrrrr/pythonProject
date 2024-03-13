import func

custlist = func.load_data()
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
    >>> ''').upper()  

    if choice=="I":        
        print("고객 정보 입력")
        page = func.insert_data(custlist)
    elif choice=="C":
        print("현재 고객 정보 조회")
        func.current_data(custlist,page)
    elif choice == 'P':
        print("이전 고객 정보 조회")
        page = func.before_data(custlist,page)
    elif choice == 'N':
        print("다음 고객 정보 조회")
        page = func.next_data(custlist,page)
    elif choice=='D':
        print("고객 정보 삭제")
        func.delete_data(custlist)
    elif choice=="U": 
        print("고객 정보 수정")
        func.modify_data(custlist)
    elif choice=="Q":
        print("프로그램 종료")
        func.save_data(custlist)
        break
