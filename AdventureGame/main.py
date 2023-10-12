from Classes.GameState import GameState


# Main loop
def main():
    current_state = GameState()

    while current_state.state != current_state.GAME_OVER:
        if current_state.state == current_state.MAIN_MENU:
            current_state.handle_main_menu()

        elif current_state.state == current_state.EXPLORATION:
            current_state.handle_exploration()

print("Tja")
# Initialize
if __name__ == "__main__":
    main()
