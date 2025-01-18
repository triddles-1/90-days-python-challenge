import json
people_string = '''{
  "people": [
    {
      "email": "john.doe@example.com",
      "name": "John Doe",
      "school": "Harvard University",
      "number": "123-456-7890"
    },
    {
      "email": "jane.smith@example.com",
      "name": "Jane Smith",
      "school": "Stanford University",
      "number": "987-654-3210"
    },
    {
      "email": "michael.brown@example.com",
      "name": "Michael Brown",
      "school": "MIT",
      "number": "555-123-4567"
    },
    {
      "email": "emily.davis@example.com",
      "name": "Emily Davis",
      "school": "University of California, Berkeley",
      "number": "444-987-6543"
    }
  ]
}
'''
data = json.loads(people_string)
print(data)
for people in data['people']:
    print(people['name'])
