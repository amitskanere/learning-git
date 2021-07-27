alien={'color':'red','point':'5','planet':'cryptonion'}
print(alien['color'])


alien1=[1,2,3,'earth','crypton','mars']
print(alien1[3])

alien3={}
alien3['color']='blue'
alien3['point']='3'
alien3['planet']='mars'
print(alien3)

#another example
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

#example_3
user_0 = {
'username': 'amitkanere1',
'first': 'amit',
'last': 'kanere',
}
for key, value in user_0.items():
 print("\nKey: " + key)
 print("Value: " + value)