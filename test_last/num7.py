def solution(s):
    n = len(s)
    count = 0
    old = ''

    for i in range(1, (n//2)+1, 1): # 문자열의 처음부터 절반까지만 진행
        string = ''
        for j in range(0, n, i): #모두 진행 (크기 i씩 맞춰서)
            if j == 0:
                old = s[j: j + i] #equ = s[0]
            if s[j: j + i] == old: #다음문자가 저장해뒀던 이전의 equ와 같으면 count + 1
                count += 1
            #하나씩 늘려가며 가져와서 비교교

            else: #다음문자가 새로운 문자라면 진입
                if count > 1:
                    string += str(count) + old #count한적 있으면 지금까지 모은 정보를 저장
                else:
                    string += old #count한적 없으면 바로 전 문자 저장

                old = s[j: j + i] #old 저장
                count = 1 #하나 있는거니까 count 1로 초기화

        if count > 1:
            string += str(count) + old
        else:
            string += old

        count = 0
        print('{0} : {1}'.format(string, len(string)))


solution("ddddaaaaccccccff")
