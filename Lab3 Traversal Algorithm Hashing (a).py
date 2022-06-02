def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 10, 'El')
insert(HashTable, 25, 'Billy')
insert(HashTable, 20, 'Will')
insert(HashTable, 9, 'Mad Max')
insert(HashTable, 21, 'Steve')
insert(HashTable, 21, 'Mike')

display_hash(HashTable)

