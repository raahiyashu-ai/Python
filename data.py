student_data={
    "ID1":{"name":"Raahithya","class":"vii","subject_intergration":"Math,Science,English,Kannada,Hindi,Social,Sports"},
    "ID2":{"name":"Sagar","class":"vii","subject_intergration":"Math,Science,Kannada,Sports,Social,English,Hindi"},
    "ID3":{"name":"Monish","class":"vii","subject_intergration":"Math,Kannada,Sports,Science,Hindi,Social,English"},
    "ID4":{"name":"Anish","class":"vii","subject_intergration":"Math,Science,English,Kannada,Hindi,Social"},
}
result={}
seen_keys=[]
for student_ID,details in student_data.items():
    unique_key =(details["name"],details["class"],details["subject_intergration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_ID]=details
for k,v in result.items():
    print(k,":",v)