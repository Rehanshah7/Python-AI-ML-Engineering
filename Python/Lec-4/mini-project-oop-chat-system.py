from datetime import datetime

# Create a Chat system with the OOPS concepts. We have to create classes User, Message and ChatRoom. And we have to implement the functions to sending messages, veiwing chat history and user joining and leaving the chatroom.
print("Welcome to the Chat System!")
class User:
    def __init__(self, user_id, username):
        self.__user_id = user_id
        self.__username = username
        self.__joined_rooms = []

    @property
    def user_id(self):
        return self.__user_id

    @property
    def username(self):
        return self.__username

    def join_room(self, chat_room):
        if chat_room.add_user(self):
            self.__joined_rooms.append(chat_room)
            print(f"{self.username} has joined the chat room '{chat_room.room_name}'.")

    def leave_room(self, chat_room):
        if chat_room.remove_user(self):
            self.__joined_rooms.remove(chat_room)

            print(f"{self.username} left {chat_room.room_name}")

    def send_message(self, chat_room, text):
        if chat_room not in self.__joined_rooms:
            raise ValueError(f"{self.username} is not a member of "f"{chat_room.room_name}")

        chat_room.receive_message(self, text)



class Message:
    def __init__(self, sender, text, timestamp=None):
        self.__sender = sender
        self.__text = text
        self.__timestamp = timestamp if timestamp else datetime.now()

    @property
    def sender(self):
        return self.__sender

    @property
    def text(self):
        return self.__text

    @property
    def timestamp(self):
        return self.__timestamp

    def display(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.sender.username}: {self.text}"

class ChatRoom:
    def __init__(self, room_name):
        self.__room_name = room_name
        self.__users = []
        self.__messages = []

    @property
    def room_name(self):
        return self.__room_name

    def add_user(self, user):
        if user in self.__users:
            print(f"{user.username} is already in the chat room.")
            return False
        self.__users.append(user)
        system_message = SystemMessage(f"{user.username} joined the chat room.")
        self.__messages.append(system_message)

        return True

    def remove_user(self, user):
        if user not in self.__users:
            print(f"{user.username} is not in the chat room.")
            return False
        self.__users.remove(user)
        system_message = SystemMessage(f"{user.username} left the chat room.")
        self.__messages.append(system_message)
        
        return True

    def receive_message(self, sender, text):
        if sender not in self.__users:
            raise ValueError(f"{sender.username} is not a member of the room.")
        message = Message(sender, text)
        self.__messages.append(message)
        print(f"Message sent by {sender.username}")

    def view_chat_history(self):
        print(f"\n===== {self.room_name} CHAT HISTORY =====")

        if not self.__messages:
            print("No messages yet.")
            return

        for message in self.__messages:
            print(message.display())

        print("=====================================\n")

class SystemMessage(Message):
    def __init__(self, text):
        self.__text = text
        self.__timestamp = datetime.now()

    @property
    def text(self):
        return self.__text

    @property
    def timestamp(self):
        return self.__timestamp

    def display(self):
        return (f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] " f"SYSTEM: {self.text}")



rahul = User(1, "Rahul")
room = ChatRoom("Python Developers")

rahul.join_room(room)
rahul.send_message(room, "Hello!")
room.view_chat_history()
rahul.leave_room(room)


# ============================================================
#                    USER FLOW
# ============================================================

#                         USER
#                          |
#              ┌───────────┼───────────┐
#              ↓           ↓           ↓
#         join_room()  send_message()  leave_room()
#              |           |
#              ↓           ↓
#         CHAT ROOM   CHAT ROOM
#              |           |
#              |           ↓
#              |    receive_message()
#              |           |
#              |           ↓
#              |       MESSAGE
#              |           |
#              |       ┌───┼──────┐
#              |       ↓   ↓      ↓
#              |    sender text  timestamp
#              |       |
#              |       ↓
#              |      USER
#              |
#              ↓
#           __users


# ============================================================
#                    CHAT ROOM
# ============================================================

#                      CHAT ROOM
#                          |
#             ┌────────────┴────────────┐
#             ↓                         ↓
#          __users                  __messages
#             |                         |
#       ┌─────┼─────┐             ┌───────────────┐
#       ↓     ↓     ↓             ↓               ↓
#     Rahul  Priya  Amit       Message       SystemMessage
#                                  |                |
#                                  |                |
#                                  ↓                ↓
#                              sender → User      SYSTEM
#                              text               text
#                              timestamp          timestamp


# ============================================================
#                  CLASS RELATIONSHIPS
# ============================================================

#                         Message
#                            ▲
#                            |
#                        inheritance
#                            |
#                       SystemMessage
#
#
#                    ChatRoom
#                    /      \
#                   /        \
#                  ↓          ↓
#               User       Message
#
#       ChatRoom HAS-A User
#       ChatRoom HAS-A Message
#
#       SystemMessage IS-A Message


# ============================================================
#                    COMPLETE FLOW
# ============================================================

# 1. Create User
#
#       rahul = User(1, "Rahul")
#                  ↓
#                USER
#             ┌─────────┐
#             │ Rahul   │
#             │ ID: 1   │
#             └─────────┘


# 2. Create ChatRoom
#
#       room = ChatRoom("Python Developers")
#                   ↓
#               CHAT ROOM
#       ┌──────────────────┐
#       │ Python Developers│
#       │                  │
#       │ Users: []        │
#       │ Messages: []     │
#       └──────────────────┘


# 3. User joins
#
#       rahul.join_room(room)
#                ↓
#             ChatRoom
#                |
#                ↓
#             __users
#                |
#                ↓
#              Rahul
#
#       A SystemMessage can also be created:
#
#       SYSTEM: Rahul joined the room.


# 4. User sends message
#
#       rahul.send_message(room, "Hello!")
#                ↓
#             ChatRoom
#                |
#                ↓
#         receive_message()
#                |
#                ↓
#             Message
#                |
#        ┌───────┼────────┐
#        ↓       ↓        ↓
#      Rahul   Hello!   timestamp
#                ↓
#       Stored in __messages


# 5. View chat history
#
#       room.view_chat_history()
#                   ↓
#              __messages
#                   |
#          ┌────────┼─────────┐
#          ↓                  ↓
#       Message           SystemMessage
#          |                  |
#          ↓                  ↓
#       display()         display()
#          |                  |
#          └────────┼─────────┘
#                   ↓
#              Chat History


# 6. User leaves
#
#       rahul.leave_room(room)
#                ↓
#             ChatRoom
#                |
#                ↓
#          remove_user()
#                |
#                ↓
#             __users
#                |
#             Rahul removed
#
#       A SystemMessage can also be created:
#
#       SYSTEM: Rahul left the room.

