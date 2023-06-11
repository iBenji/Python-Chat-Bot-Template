from tkinter import *

def open_chat():
    # Create a new window for the AI Coding chat
    chat_window = Toplevel()
    chat_window.title("AI Coding Chat")

    # Create a Text widget to display chat history
    chat_history = Text(chat_window, state=DISABLED)
    chat_history.pack(expand=True, fill=BOTH)

    # Set the background color and font color for the chat history
    chat_history.configure(bg='#505050', fg='white')

    # Configure tags to change the text color for messages from "You" and "Python Bot"
    chat_history.tag_config('you', foreground='yellow')
    chat_history.tag_config('bot', foreground='red')

    # Create an Entry widget to enter messages
    message_input = Entry(chat_window)
    message_input.pack(side=BOTTOM, fill=X)

    # Function to add messages to the chat history
    def add_message(message, tag):
        chat_history.configure(state=NORMAL)
        chat_history.insert(END, message + '\n', tag)
        chat_history.configure(state=DISABLED)

    # Function to process a message and generate a response
    def process_message():
        message = message_input.get()
        message_input.delete(0, END)

        # TODO: implement AI bot logic here ig?

        response = "I'm brainless Python Bot! I can't do anything, so you have to implement me some braincells"
        add_message("You: " + message, 'you')
        add_message("Python Bot: " + response, 'bot')

    # Bind the Enter key to send messages
    message_input.bind('<Return>', lambda event: process_message())

root = Tk()

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a file menu with a "Exit" option
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Python Bot", menu=file_menu)

# Create a submenu with options
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label="AI Coding", command=open_chat)
file_menu.add_cascade(label="Options", menu=sub_menu)

# Create a label
my_label = Label(root, text="Welcome to Python Bot")
my_label.pack()

# Get the size of the content
x = root.winfo_reqwidth()
y = root.winfo_reqheight()

# Set the geometry of the window based on the size of the content
root.geometry('{}x{}'.format(x, y))

root.mainloop()