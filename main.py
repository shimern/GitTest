import requests
import pytest
import time

get_count= {
    "version": "1.2.0.1",
    "filter": {}
}

get_list = {
        "version" : "1.2.0.1",
        "pagination" : {
            "count" : 20,
            "number" : 1,
            "random" : "false",
            "sort" : "lastname",
            "orderDesc": "false"
            }
}
bad_request_1={
    "version": "1.2.0.1",
    "pagination": {
        "count": 20,
        "number": -1,
        "random": "false",
        "sort": "lastname",
        "orderDesc": "false"
    }
}

bad_request_2={
        "version" : "1.2.0.1",
        "pagination" : {
            "count" : 20,
            "number" : "qwd",
            "random" : "false",
            "sort" : "lastname",
            "orderDesc": "false"
            }
}
bad_request_3={
        "version" : "1.2.0.1",
        "pagination" : {
            "count" : 20,
            "number" : 50,
            "random" : "false",
            "sort" : "lastname",
            "orderDesc": "false"
            }
}

check_initial_request={

}

LIST_URL = 'http://192.168.0.16:8080/students/general/get-student-list'
COUNT_URL = 'http://192.168.0.16:8080/students/general/get-student-count'
CHECK_INITIAL_URL='http://192.168.0.16:8080/students/general/5'

def test_get_student_list():
    start_time=time.time()
    response = requests.post(f'{LIST_URL}', json=get_list)
    end_time = time.time()
    assert response.status_code==200
    print("test_get_student_list завершился удачно за", end_time - start_time, "секунд")
def test_bad_request1_get_student_list():
    start_time=time.time()
    response = requests.post(f'{LIST_URL}', json=bad_request_1)
    end_time = time.time()
    assert response.status_code==500
    print("test_bad_request1_get_student_list завершился удачно за", end_time - start_time, "секунд")
def test_bad_request2_get_student_list():
    start_time=time.time()
    response = requests.post(f'{LIST_URL}', json=bad_request_2)
    end_time = time.time()
    assert response.status_code==400
    print("test_bad_request2_get_student_list завершился удачно за", end_time - start_time, "секунд")
def test_bad_request3_get_student_list():
    start_time=time.time()
    response = requests.post(f'{LIST_URL}', json=bad_request_3)
    end_time = time.time()
    assert response.status_code==200
    print("test_bad_request3_get_student_list завершился удачно за", end_time - start_time, "секунд")
def test_get_student_count():
    start_time=time.time()
    response = requests.post(f'{COUNT_URL}', json=get_count)
    end_time = time.time()
    assert response.status_code==200
    print("test_get_student_count завершился удачно за", end_time - start_time, "секунд")

def create_fullname(lastname, firstname, middlename):
    initial = middlename[0].upper() + "." if middlename else ""
    initial_name = firstname[0].upper() + "."
    full_name = lastname.capitalize() + " " + initial_name + initial
    return full_name


def test_check_initial(withPatronymic=True):
    start_time=time.time()
    response = requests.get(f'{CHECK_INITIAL_URL}', json=get_count)
    end_time = time.time()
    assert response.status_code==200
    print("test_check_initial завершился удачно за", end_time - start_time, "секунд")

    data=response.json()

    initials=create_fullname(
        data["info"][0]["personalData"]["lastname"],
        data["info"][0]["personalData"]["firstname"],
        data["info"][0]["personalData"]["patronymic"],
    )

    if data["info"][0]["personalData"]["lastnameInitials"] == initials:
        print("Отображение корректное")
    else:
        print("Отображение некорректное")



if __name__ == "__main__":
    pytest.main([__file__])
    test_get_student_count()
    test_get_student_list()
    test_bad_request1_get_student_list()
    test_bad_request2_get_student_list()
    test_bad_request3_get_student_list()
    test_check_initial()
