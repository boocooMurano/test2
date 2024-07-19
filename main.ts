player.onChat("tp", function () {
    agent.teleportToPlayer()
})
player.onChat("mae", function () {
    agent.teleportToPlayer()
    agent.setItem(STONE, 100, 1)
    for (let index = 0; index < 20; index++) {
        agent.move(FORWARD, 1)
        agent.place(DOWN)
        agent.move(RIGHT, 1)
        agent.place(DOWN)
    }
})
