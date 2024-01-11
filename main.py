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
            "number" : 0,
            "random" : "false",
            "sort" : "lastname",
            "orderDesc": "false"
            }
}



LIST_URL = 'http://192.168.0.16:8080/students/general/get-student-list'
COUNT_URL = 'http://192.168.0.16:8080/students/general/get-student-count'

def test_get_student_list():
    start_time=time.time()
    response = requests.post(f'{LIST_URL}', json=get_list)
    end_time = time.time()
    assert response.status_code==200
    print("test_get_student_list завершился удачно за", end_time - start_time, "секунд")
def test_get_student_count():
    start_time=time.time()
    response = requests.post(f'{COUNT_URL}', json=get_count)
    end_time = time.time()
    assert response.status_code==200
    print("test_get_student_count завершился удачно за", end_time - start_time, "секунд")


if __name__ == "__main__":
    pytest.main([__file__])
    test_get_student_count()
    test_get_student_list()