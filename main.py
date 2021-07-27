print("이차함수의 꼭짓점과 이차방정식의 두 근을 구하는 프로그램입니다.\n 이차식을 요구사항과 같이 입력해 주세요.\n")

degree_2 = float(input('이차항을 실수형으로 입력해 주세요.')) #이차항을 입력받음
degree_1 = float(input('일차항을 실수형으로 입력해 주세요.')) #일차항을 입력받음
degree_0 = float(input('상수항을 실수형으로 입력해 주세요.')) #상수항을 입력받음

print("\n입력받은 이차식은 %dX^2 + %dX + %d 입니다" %(degree_2,degree_1,degree_0)) #이차식을 출력한다

print("\n꼭짓점 공식으로 꼭짓점을 구합니다")

vertex_1_x = ( (-1 * degree_1) / (2 * degree_2 )) #꼭짓점 공식으로 이차함수의 꼭짓점의 X값을 구한다
vertex_1_y = ( degree_2 * vertex_1_x * vertex_1_x + degree_1 * vertex_1_x + degree_0) #이차식에 X값을 대입하여 Y값을 구한다

print("결과 - X = %f , Y = %f\n\n" %( vertex_1_x , vertex_1_y )) #결과값 출력 - 100%정확

print("완전 제곱식으로 꼭짓점을 구합니다")

tmpdgree_1 = degree_1/degree_2 #이차항으로 식을 나눠주는 과정
tmpdgree_0 = degree_0/degree_2


vertex_2_x = -1 * (tmpdgree_1 / 2) #반의 제곱법칙을 이용하여 완전제곱식의 근을 유도한다
vertex_2_y = -1 * ((-1 * tmpdgree_0) + (vertex_2_x * vertex_2_x)) #상수항을 우변으로 이항하여 완전제곱식의 여를 이항하여 더해준다

print("결과 - X = %f , Y = %f\n\n" %( vertex_2_x , vertex_2_y ))#100% 정확하지 않음, 이차항의 계수가 1이 아닐 경우 예상한 값이 나오지 않음.


print('-5 ~ 5  를 산출하여 최대의 y와 최소의 y를 구합니다') #브루트 포스(무조건대입)를 이용한 식의 최솟값 계산


a = list() #무조건대입을 위한 값을 저장할 배열 선언
b = list() #산출값을 위한 값을 저장할 배열 선언

for i in range(-5,6): # 무조건 대입을 위한 반복문 실행
    a.append( degree_2 * i * i + degree_1 * i + degree_0)
    b.append(degree_2 * i * i + degree_1 * i + degree_0)

a.sort()

max_y = a[ len(a)-1 ];
min_y = a[0]

print(b)


max_x_arr = list()
min_x_arr = list()

for j in range(-5,6): #X의 최대 최소 값을 구한다
    if b[j+5] == max_y:
        max_x_arr.append(j)
    elif(b[j+5]) == min_y:
        min_x_arr.append(j)

print(max_x_arr) #배열을 출력
print(min_x_arr) 

print('해당 함수의 최댓값 Y는 X가 %f 일때 %f 이고, 최솟값은 X가 %f 일때 %f입니다'%( max_x_arr[0] ,max_y,min_x_arr[0]  ,min_y)) #결과 산출,  범위 내에서는 100%정확


#참고
#https://ko.m.wikihow.com/이차방정식의-근-구하는-법
#https://ko.wikihow.com/이차방정식의-꼭짓점-구하는-방법