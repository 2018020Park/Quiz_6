def quiz6(o):
    while True:
        m = input("주민번호 13자리를 입력하세요. (- 제외): ")
        if len(m) != 13 or not m.isdigit():
            print("유효하지 않은 입력입니다. 13자리의 숫자를 입력하세요.")
            continue

        x = list(map(int, m))

        c = 2
        d = 2
        y = 0
        i = 0

        for a in x[0:8]:
            y += c * a
            c += 1

        for v in x[8:12]:
            i += d * v
            d += 1

        k = y + i
        l = k % 11
        p = 11 - l


        if p != x[12]:
            print("주민등록번호가 유효하지 않습니다. 다시 입력해주세요.")
        else:
            print("주민등록번호가 유효합니다.")
            break

r = input("주민번호 프로그램을 실행하시겠습니까? (o 또는 x 입력): ")
if r == "o" or r == "O" or r == "0":
    quiz6(None)
elif r == "x" or r == "X":
    print("프로그램을 종료합니다.")

