#더하기 빼기 곱하기 나누기 나머지 몫
#+ - * / % //
#예시 7 / 5 =
# print() 들어간 값을 출력해주는 함수
#7 // 5 몫
#7 % 5  나머지
#변수
# 변수의 이름 = 넣을 값
# a = 7
# # b = -11
# # b=a
# #a=a+1
# a +=1
# print(a)
# c= a*b
# print(a)
# print(a+2)
# print(a+b)
# print(c)
# print(a,b)
# a=7
# b=3
# c=b
# b=a
# a=c
# print(a,b)
# a=3
# b=6
# c=9
# f=c
# c=b
# b=a
# a=f
# print(a,b,c)
# 자료형
# a=7 #정수 - int  integral
# b=3.1 #실수 - float
# c= "abcd"#문자열 - str  string
# #type() 들어간 값의 자료형을 알려줌
# print(type(c))

#문자열
# a="hello"
# b="good bye"
# c=a+b
# print(c)

#인덱싱, 슬라이싱
# a="WELCOME!"
# # print(a[:3]) 3미만
# #print(a[4:]) 4이상
# print(a[2:5])

# a="hallo pithon?"
# b="he"
# d="ython!"
# c=b+a[2:7]
# print(c+d)
# print(a[0]+"e"+a[2:7]+"y"+a[8:12]+"!")

#bool -참과 거짓= True or False
# a = True
# b = False
# print(a,b)

#조건문
# if 조건: 조건이 참일 때 실행할 코드



#논리연산자 and: 묶인 조건이 모두 참일 때만 참 or: 묶인 조건들중에 하나라도 참이면 참 ==: 같다면 !=: 같지 않다면 < > <= >=
# a=9
# if a == 8:
#     print(a+3)
#     a=a+12
# print(a)

#else - if 조건문이 거짓일 때 실행
# a=9
# if a == 8:
#     print(a+3)
#     a=a+12
# else:
#     print(a-3)
# print(a)

#elif - if 조건문이 거짓일 때, 그리고 자신의 조건이 참일 떄 실행

# a=9
# if a == 8 and != 9:
#     print(a+3)
#     a=a+12
#     if a>2:
#     print(a-21)
# elif a>=4 or a<=3:
#     print(a*3)
# else:
#     print(a-3)
#
#
# print(a)

#입력함수 -input()
# a=input()
# print(a)

# print(type(a)) #숫자를 넣어도 문자열로 입력한다.
# a=int(input()) #문자열로 받은 숫자를 정수형 값으로 바꿈
# print(a)
# print(type(a))


#숫자값을 입력받아 그 숫자가 홀수라면 "홀"을, 짝수라면 "짝"을 출력

# a=int(input())
#
# print(a)
#
# if a%2==0:
#     print("짝")
# if a%2!=0:
#     print("홀")


# 세 수를 입력받아 모두 곱해서 출력하기
# a=int(input())
# b=int(input())
# c=int(input())
#
# print(a*b*c)


#세자리 수를 받아서 백의 자리, 십의 자리, 일의 자리를 각각 뽑아내어 출력하기

# a=(input())
#
# print(a)

#슬라이싱
# print("백의 자리:",a[:1])
# print("십의 자리:",a[1:2])
# print("일의 자리:",a[2:])

#인덱싱
# print("백의 자리:",a[0])
# print("십의 자리:",a[1])
# print("일의 자리:",a[2])

#숫자를 이용한 고난이도 방법

# a=int(input())
# print(a%10)
# b=a//10
# print(b%10)
# c=b//10
# print(c%10)



#세자리 수의 두 수가 주어짐. 두번째 수의 각 자리수를 첫번째 수의 각각 곱해서 따로 출력,마지막에 두 수를 곱한 값을 출력

# b=int(input())
# a=(input())
#
# print(b,a)
#
# print(int(a[0])*b)
# print(int(a[1])*b)
# print(int(a[2])*b)
# print(int(a)*b)



# print(a%10*b)
# c=a//10
# print(c%10*b)
# d=c//10
# print(d%10*b)
# print(a*b)