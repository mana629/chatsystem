# chat machine / massage chat system
class ChatMachine:
    massage_count = 1

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = massge.massage_count
        massge.massage_count += 1

    def __str__(self):
        return f"Massage {self.id} from {self.sender}: {self.content}"


class User:
    def __init__(self, name):
        self.name = name
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.name} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.name} joined the chatroom.")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.name} is leaving chatroom.")
        else:
            if self.chatroom.remove_user(self):
                self.chatroom = None
                print(f"{self.name} left the chatroom.")

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.name} is not in a chatroom.")
        else:
            self.chatroom.broadcast_message(self, content)


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self_users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast_message(self, sender, content):
        message = ChatMachine(sender, content)
        self.messages.append(message)
        return message

    def show_chat_history(self):
        print(f"Chat history for {self.name}:")
        for message in self.messages:
            print(message)
# chat machine / massage chat system
class ChatMachine:
    massage_count = 1

    def __init__(self,sender,content):
        self.sender = sender
        self.content = content
        self.id = massge.massage_count
        massge.massage_count += 1


    def __str__(self):
        return f"Massage {self.id} from {self.sender}: {self.content}"


class User:
    def __init__(self,name):
        self.name = name
        self.chatroom = None 

    def join_chatroom(self,chatroom):
        if self.chatroom:
            print(f"{self.name} is already in a chatroom.")

        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.name} joined the chatroom.")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.name} is leaving chatroom.")
        else:
            if self.chatroom.remove_user(self):
                self.chatroom = None
                print(f"{self.name} left the chatroom.")

    def send_message(self,content):
        if not self.chatroom:
            print(f"{self.name} is not in a chatroom.")
        else:
            self.chatroom.broadcast_message(self,content)


class ChatRoom:
    def __init__(self,name):
        self.name = name
        self.users = []
        self.messages = []
    def add_user(self,user):
        self_users.append(user)


    def remove_user(self,user):
        self.users.remove(user)


    def broadcast_message(self,sender,content):
        message = ChatMachine(sender,content)
        self.messages.append(message)
        return message

    def show_chat_history(self):
        print(f"Chat history for {self.name}:")
        for message in self.messages:
            print(message)  

        
 

 