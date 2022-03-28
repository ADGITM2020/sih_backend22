## Localhost

```sh
curl -X 'POST' \
  'localhost:8000/institute/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_email": "adgitm@gmail.com",
  "institute_password": "123456",
  "institute_address": "shastri park, new delhi, india",
  "is_institute_parent": true,
  "is_institute_resource": true
}'

curl -X 'POST' \
  'localhost:8000/institute/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_email": "dtu@gmail.com",
  "institute_password": "123456",
  "institute_address": "DTU campus, new delhi, india",
  "is_institute_parent": true,
  "is_institute_resource": true
}'

curl -X 'POST' \
  'localhost:8000/institute/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_email": "iitdelhi@gmail.com",
  "institute_password": "123456",
  "institute_address": "IIT campus, new delhi, india",
  "is_institute_parent": true,
  "is_institute_resource": true
}'


curl -X 'POST' \
  'localhost:8000/student/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_name": "Student 1",
  "student_email": "student@gmail.com",
  "student_password": "123456",
  "institute_id": 1
}'

curl -X 'POST' \
  'localhost:8000/student/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_name": "Student 2",
  "student_email": "student2@gmail.com",
  "student_password": "123456",
  "institute_id": 1
}'


curl -X 'POST' \
  'localhost:8000/student/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_name": "Student 3",
  "student_email": "student3@gmail.com",
  "student_password": "123456",
  "institute_id": 1
}'

curl -X 'POST' \
  'localhost:8000/equipment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "equipment_name": "test tubes",
  "description": "for doing chemistry work",
  "experiments": []
}'

curl -X 'POST' \
  'localhost:8000/equipment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "equipment_name": "beaker",
  "description": "for doing chemistry work",
  "experiments": []
}'


curl -X 'POST' \
  'localhost:8000/equipment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "equipment_name": "welding",
  "description": "for doing metal work",
  "experiments": []
}'


curl -X 'POST' \
  'localhost:8000/equipment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "equipment_name": "smelting machine",
  "description": "for doing metal work",
  "experiments": []
}'


curl -X 'POST' \
  'localhost:8000/experiment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "aim": "ph level of water",
  "description": "To test ph level of water",
  "equipments": [1,2]
}'


curl -X 'POST' \
  'localhost:8000/experiment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "aim": "welding two metals",
  "description": "To weld two metals and check strength",
  "equipments": [3,4]
}'

curl -X 'POST' \
  'localhost:8000/lab/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_id": 1,
  "lab_name": "chemistry lab",
  "lab_address": "room no. 12",
  "lab_student_capacity": 60,
  "lab_admin_name": "Dr. Kavita"
}'

curl -X 'POST' \
  'localhost:8000/lab/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_id": 1,
  "lab_name": "welding lab",
  "lab_address": "room no. 30",
  "lab_student_capacity": 20,
  "lab_admin_name": "Mr Mukesh"
}'

curl -X 'POST' \
  'localhost:8000/slot/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_id": 1,
  "lab_id": 1,
  "start_time": "09:30:26",
  "end_time": "10:30:26"
}'

curl -X 'POST' \
  'localhost:8000/slot/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_id": 1,
  "lab_id": 1,
  "start_time": "10:30:26",
  "end_time": "11:30:26"
}'
```

## Azure

```sh
curl -X 'POST' \
  'https://www.sihbackend.tech/institute/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_email": "adgitm@gmail.com",
  "institute_password": "123456",
  "institute_address": "shastri park, new delhi, india",
  "is_institute_parent": true,
  "is_institute_resource": true
}'

curl -X 'POST' \
  'https://www.sihbackend.tech/institute/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_email": "dtu@gmail.com",
  "institute_password": "123456",
  "institute_address": "DTU campus, new delhi, india",
  "is_institute_parent": true,
  "is_institute_resource": true
}'

curl -X 'POST' \
  'https://www.sihbackend.tech/institute/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_email": "iitdelhi@gmail.com",
  "institute_password": "123456",
  "institute_address": "IIT campus, new delhi, india",
  "is_institute_parent": true,
  "is_institute_resource": true
}'


curl -X 'POST' \
  'https://www.sihbackend.tech/student/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_name": "Student 1",
  "student_email": "student@gmail.com",
  "student_password": "123456",
  "institute_id": 1
}'

curl -X 'POST' \
  'https://www.sihbackend.tech/student/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_name": "Student 2",
  "student_email": "student2@gmail.com",
  "student_password": "123456",
  "institute_id": 1
}'


curl -X 'POST' \
  'https://www.sihbackend.tech/student/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_name": "Student 3",
  "student_email": "student3@gmail.com",
  "student_password": "123456",
  "institute_id": 1
}'

curl -X 'POST' \
  'https://www.sihbackend.tech/equipment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "equipment_name": "test tubes",
  "description": "for doing chemistry work",
  "experiments": []
}'

curl -X 'POST' \
  'https://www.sihbackend.tech/equipment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "equipment_name": "beaker",
  "description": "for doing chemistry work",
  "experiments": []
}'


curl -X 'POST' \
  'https://www.sihbackend.tech/equipment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "equipment_name": "welding",
  "description": "for doing metal work",
  "experiments": []
}'


curl -X 'POST' \
  'https://www.sihbackend.tech/equipment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "equipment_name": "smelting machine",
  "description": "for doing metal work",
  "experiments": []
}'


curl -X 'POST' \
  'https://www.sihbackend.tech/experiment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "aim": "ph level of water",
  "description": "To test ph level of water",
  "equipments": [1,2]
}'


curl -X 'POST' \
  'https://www.sihbackend.tech/experiment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "aim": "welding two metals",
  "description": "To weld two metals and check strength",
  "equipments": [3,4]
}'

curl -X 'POST' \
  'https://www.sihbackend.tech/lab/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_id": 1,
  "lab_name": "chemistry lab",
  "lab_address": "room no. 12",
  "lab_student_capacity": 60,
  "lab_admin_name": "Dr. Kavita"
}'

curl -X 'POST' \
  'https://www.sihbackend.tech/lab/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "institute_id": 1,
  "lab_name": "welding lab",
  "lab_address": "room no. 30",
  "lab_student_capacity": 20,
  "lab_admin_name": "Mr Mukesh"
}'

curl -X 'POST' \
  'https://www.sihbackend.tech/slot/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_id": 1,
  "lab_id": 1,
  "start_time": "09:30:26",
  "end_time": "10:30:26"
}'

curl -X 'POST' \
  'https://www.sihbackend.tech/slot/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "student_id": 1,
  "lab_id": 1,
  "start_time": "10:30:26",
  "end_time": "11:30:26"
}'
```