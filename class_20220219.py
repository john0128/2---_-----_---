# # # # # # # # # # station = 11
# # # # # # # # # # gettime = 37
# # # # # # # # # # sum_ = 37/11
# # # # # # # # # # print("%.2f분" % sum_)
# # # # # # # # # flt = 123.567
# # # # # # # # # print("round(flt) : ", round(flt))
# # # # # # # # # print("round(flt,1) : ", round(flt,1))
# # # # # # # # # print("round(flt,2) : ", round(flt,2)) # 반올림하는 함수
# # # # # # # # # .2f는 출력만을 담당하지만 round()는 값을 가공한다
# # # # # # # # #
# # # # # # # # 틀린 답
# # # # # # # # hotelfloorheight = 2.6
# # # # # # # # floorsu = 14
# # # # # # # # firstfloorheight = 500.23
# # # # # # # # sum_1 = hotelfloorheight * floorsu
# # # # # # # # sum_2 = sum_1 - 1
# # # # # # # # sum_3 = sum_2 + firstfloorheight
# # # # # # # # print("%.3fm" % sum_3)
# # # # # # # #
# # # # # # # 맞는 답
# # # # # # # avg_height = 260
# # # # # # # to_fl = 14
# # # # # # # one_fl = 500.23
# # # # # # # to_height = avg_height*(to_fl-1)+one_fl
# # # # # # # meter = to_height / 100
# # # # # # # print("호텔의 총 높이 : ", round(meter,3),"m")
# # # # # # org_length = 100
# # # # # # to100m = 11.27
# # # # # # to1h1 = 3600 / 11.27
# # # # # # to1hround = round(to1h1,2)
# # # # # # to1_lengthm = to1hround * org_length
# # # # # # to1_lengthkm = to1_lengthm / 1000
# # # # # # to1lgkmrd = round(to1_lengthkm,2)
# # # # # # print(to1lgkmrd, "m")
# # # # # flt = 123.123
# # # # # print("%.3f + %.3f = %.3f" % (flt,321.321,flt+321.321))
# # # # # print(flt, "+", 321.321,"=",flt+321.321)
# # # # # ch1,ch2,ch3 = "파", "2", "썬"
# # # # # print("%c + %c + %c = %s" % (ch1, ch2, ch3, ch1+ch2+ch3))
# # # # # print(ch1, "+", ch2, "+", ch3, "=", ch1+ch2+ch3)
# # # # # str_1 = "python"
# # # # # str_2 = "test"
# # # # # str_3 = str_1 + str_2
# # # # # print("%s + %s = %s" % (str_1, str_2, str_1+str_2))
# # # # # print(str_1, "+", str_2, "=", str_1+str_2)
# # # # # 컴퓨터 언어의 자료형
# # # # # 숫자 (정수, 실수)
# # # # # 문자열
# # # # # 리스트, 튜플, 딕셔너리, set
# # # # # 자료형과 + 연산자의 규칙
# # # # # 숫자 + 숫자 (덧셈 연산)
# # # # # 문자열 + 문자열
# # # # # 리스트 + 리스트
# # # # # 튜플 + 튜플
# # # # # 은 하나로 합치는 연산이 진행됨
# # # # # 같은 자료형의 연산만 가능합니다
# # # # # 리스트 + 문자열 X(불가능)
# # # # A = 10
# # # # B = 5
# # # # print("type : ", type(A<B));print("type : ", (A<B))
# # # # num = 100;print("type : %s" % type(num))
# # # # flt = 321.321;print("type : %s" % type(flt))
# # # # ch = "A";print("type : %s" % type(ch))
# # # # st = "test";print("type : %s" % type(st))
# # # # type라는 함수는 데이터의 자료형을 반환하는 함수이다
# # # num = 100
# # # print("type : %s\tid : %s" % (type(num),id(num)))
# # # num = 321.321
# # # print("type : %s\tid : %s" % (type(num),id(num)))
# # # num = "A"
# # # print("type : %s\tid : %s" % (type(num),id(num)))
# # # num = "test"
# # # print("type : %s\tid : %s" % (type(num),id(num)))
# # st1 = "Python"
# # st2 = "Test"
# # su = 100
# # flt = 1.11
# # num = '100'
# # print(flt+su)
# # print(st1 + st2)
# # print(su+num)
# su = 100
# print('type(su) : ', type(su))
# print('type(str(su)) : ', type(str(su)))
# print('type(float(su)) : ' type(float(su)))
# int, str, float는 자료형을 지정하는 함수이다
# 어떤 자료형이든 문자열 변경은 무조건 가능하다
# 하지만 다른 자료형 변경은 다 되는 것은 아니다
# 그리고 함수를 이용해서 변경한 자료형 변경은 1회성이다
