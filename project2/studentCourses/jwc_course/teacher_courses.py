from studentCourses.jwc_course.login import check_valid

username = input()
password = input()
ret = check_valid(username, password)
print(ret)