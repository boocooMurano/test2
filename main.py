def on_on_chat():
    agent.teleport_to_player()
player.on_chat("tp", on_on_chat)

def on_on_chat2():
    agent.teleport_to_player()
    agent.set_item(STONE, 100, 1)
    for index in range(20):
        agent.move(FORWARD, 1)
        agent.place(DOWN)
        agent.move(RIGHT, 1)
        agent.place(DOWN)
player.on_chat("mae", on_on_chat2)
