import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()

# @pytest.fixture
# def students_factory():
#     def factory(*args, **kwargs):
#         return baker.make(Student, *args, **kwargs)
#     return factory


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_course(client, courses_factory):
    courses = courses_factory(_quantity = 10)
    response = client.get('/api/v1/courses/1/')
    data = response.json()

    assert data['id'] == courses[0].id

@pytest.mark.django_db
def test_get_list_course(client, courses_factory):
    courses = courses_factory(_quantity = 10)
    response = client.get('/api/v1/courses/')
    data = response.json()

    assert len(data) == len(courses)

@pytest.mark.django_db
def test_get_filter_id_course(client, courses_factory):
    courses = courses_factory(_quantity = 10)
    response = client.get('/api/v1/courses/?id=21')
    print(response.json())
    data = response.json()

    assert data[0]['id'] == 21

@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/api/v1/courses/', data={'name': 'Химия'}, format='json')

    assert response.status_code == 201

@pytest.mark.django_db
def test_get_filter_name_course(client, courses_factory):
    courses = courses_factory(_quantity=10)
    name = courses[0].name
    resp = client.get(f'/api/v1/courses/?name={name}')
    data = resp.json()

    assert data[0]['name'] == name

@pytest.mark.django_db
def test_get_patch_course(client, courses_factory):
    courses = courses_factory(_quantity=10)
    course_id = courses[0].id
    resp = client.patch(f'/api/v1/courses/{course_id}/', data={"name": "Измененно на Химия"}, format='json')
    data = resp.json()

    assert data["name"] == "Измененно на Химия"

@pytest.mark.django_db
def test_get_delete_course(client, courses_factory):
    courses = courses_factory(_quantity=10)
    course_id = courses[0].id
    resp = client.delete(f'/api/v1/courses/{course_id}/')

    assert resp.status_code == 204