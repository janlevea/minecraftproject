#*****************************************************  
# lesson9_python_makecode.py
# @author tekija: Jani L
# @since pvm: 9.5.2023
# @version versio: 1
#*****************************************************/ 
# Make agent shoot blocks above
def shootBlocks():
    # Declare score variable as global                                                          |Act. 3 
    global score  
    # If conditional, test for block condition, Agent pos + 2                                   |Act. 2 Part 1
    if blocks.test_for_block(GOLD_BLOCK, positions.add(agent.get_position(), pos(0, +2, 0))):
        # Spawn firework rockets at Agent position                                              |Act. 2 Part 1
        mobs.spawn(FIREWORKS_ROCKET, agent.get_position())
        # Pause for 100ms                                                                       |Act. 2 Part 1
        loops.pause(100)
        # Place AIR block at Agent pos + 2                                                      |Act. 2 Part 1
        blocks.place(AIR, positions.add(agent.get_position(), pos(0, +2, 0)))
        # Add 1 to the variable score                                                           |Act. 3
        score += 1
    # Elif conditional, test for block condition, Agent pos + 3                                 |Act. 2 Part 2
    elif blocks.test_for_block(GOLD_BLOCK, positions.add(agent.get_position(), pos(0, +3, 0))):
    # Spawn firework rockets at Agent position                                                  |Act. 2 Part 2
        mobs.spawn(FIREWORKS_ROCKET, agent.get_position())
        # Pause for 100ms                                                                       |Act. 2 Part 2
        loops.pause(100)
        # Place AIR block at Agent pos + 3                                                      |Act. 2 Part 2
        blocks.place(AIR, positions.add(agent.get_position(), pos(0, +3, 0)))
        # Add 1 to the variable score                                                           |Act. 3
        score += 1
# Check if player is standing on blue or red block and move agent to direction
def moveAgent():
    if blocks.test_for_block(LIGHT_BLUE_CONCRETE, pos(0, -1, 0)):
        agent.move(RIGHT, 1)
    elif blocks.test_for_block(RED_CONCRETE, pos(0, -1, 0)):
        agent.move(LEFT, 1)

score = 0
# Add a start splash screen using the gameplay title command                                    |Act. 3
gameplay.title(mobs.target(NEAREST_PLAYER), "Agent Invader", "Peli alkaa")
# Change while loop to only loop when score is <= 15                                            |Act. 3
while True:
    if score <= 15:
        moveAgent()
        shootBlocks()
    else:
        break
# Add a end splash screen using the gameplay title command                                      |Act. 3
gameplay.title(mobs.target(NEAREST_PLAYER), "Agent Invader", "Peli päättyy")
# Spawn lighting bolt on Agent position                                                         |Act. 3  
mobs.spawn(LIGHTNING_BOLT, agent.get_position())
if score > 15:
    player.execute("scoreboard players set @p score 15")