class Key:
    def __init__(self, key_type):
        self.key_type = key_type


class Lock:
    def __init__(self, lock_type):
        self.lock_type = lock_type

    def otevri(self, key):
        if key.key_type == self.lock_type:
            print("Zámek byl úspěšně otevřen.")
        else:
            print("Klíč neodpovídá typu zámku.")



key1 = Key("klasicky")
key2 = Key("bezpecnostni")
lock1 = Lock("klasicky")
lock2 = Lock("bezpecnostni")

lock1.otevri(key1)  
lock1.otevri(key2) 
lock2.otevri(key2)  