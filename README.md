# Chess Tournament Management System

## Overview

The Chess Tournament Management System is designed to efficiently manage players, tournaments, and generate comprehensive reports related to tournaments and player statistics. The system is structured into several controllers and views, each responsible for different aspects of the management process.

## Project Structure

The project is organized into the following main components:

### Controllers
- **MainController**: Handles the main menu and navigation to different sections (Players, Tournaments, Reports).
- **PlayerController**: Manages player-related actions such as adding and listing players.
- **ReportsController**: Generates various reports about players and tournaments.
- **TournamentController**: Manages tournament-related actions including creation, player registration, and round management.

### Views
- **MainView**: Displays the main menu and common messages.
- **PlayerView**: Manages player-related menus and player details.
- **ReportsView**: Handles the reports menu and report details.
- **TournamentView**: Manages tournament-related menus and tournament details.
- **MatchView**: Displays match management menus and match details.
- **RoundView**: Displays round management menus and round details.

### Models
- **Entities**: Define core entities like Player, Match, Round, and Tournament.
- **Managers**: Handle data operations for entities, including database interactions.

## Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation
Install required packages:
