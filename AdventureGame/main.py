from Classes.GameState import GameState


# Main loop
def main():
    # TODO Create player object
    # TODO Let user choose player name
    game_state = GameState()
    print(game_state)

    while game_state.current_state != game_state.GAME_OVER:
        if game_state.current_state == game_state.MAIN_MENU:
            game_state.handle_main_menu()

        elif game_state.current_state == game_state.EXPLORATION:
            game_state.handle_exploration()


# Initialize
if __name__ == "__main__":
    main()
