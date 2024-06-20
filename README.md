# Chess Tournament Management System

## Overview

The Chess Tournament Management System is designed to manage players, tournaments, and generate reports related to tournaments and player statistics. The system is structured into several controllers and views, each responsible for different aspects of the management process.

## Project Structure

The project is organized into the following main components:

### Controllers
- **MainController**: Handles the main menu and navigation to different sections (Players, Tournaments, Reports).
- **PlayerController**: Manages player-related actions such as adding and listing players.
- **TournamentController**: Manages tournament-related actions including creation, player registration, and round management.
- **ReportsController**: Generates various reports about players and tournaments.

### Views
- **MainView**: Displays the main menu.
- **PlayerView**: Manages player-related menus.
- **ReportsView**: Handles the reports menu.
- **TournamentView**: Manages tournament-related menus.
- **RoundView**: Displays round management menus in the selected tournament.
- **MatchView**: Displays match management menus in the selected round.


### Models
- **Entities**: Define core entities like Player, Match, Round, and Tournament.
- **Managers**: Handle data operations for entities, including database interactions.

## Getting Started

### Prerequisites
- Python 3.10 or higher

### Installation
Install required packages:

pip install -r requirements.txt


## Running the Application 

Execute the main script to launch the application:

python main.py

## Usage

### Main Menu

- **Manage Players:** Navigate to player management.
- **Manage Tournaments:** Navigate to tournament management.
- **Generate Reports:** Navigate to report generation.
- **Quit:** Exit the application.

### Player Management

- **Add Player:** Add a new player to the database.
- **List All Players:** Display a list of all players.

### Tournament Management

- **Create Tournament:** Create a new tournament.
- **List All Tournaments:** Display a list of all tournaments.
- **Select Tournament:** Manage a specific tournament.

### Reports

- **List of all players in alphabetical order:** Generate and save a report of all players sorted alphabetically.
- **List of all tournaments:** Generate and save a report of all tournaments.
- **Report for a specific tournament:** Generate and save a report with details of a specific tournament.
- **List of tournament players in alphabetical order:** Generate and save a report of players in a specific tournament, sorted alphabetically.
- **List of all rounds and matches in a tournament:** Generate and save a report of all rounds and matches in a specific tournament.

## Code Structure

### MainController

Handles navigation between different sections of the application.

### PlayerController

Manages player-related actions including adding players and listing all players.

### ReportsController

Generates reports about players and tournaments.

### TournamentController

Manages tournament-related actions including creation, player registration, and round management.

### Views

Responsible for displaying menus and user interfaces for the respective controllers.


## Running flake8 and Generating HTML Report

To maintain code quality, run flake8 with a line length limit of 119 characters and generate an HTML report.

### Install flake8

pip install flake8

## Create .flake8 configuration file

Create a `.flake8` file with the following content:

[flake8]
max-line-length = 119

## Run flake8 and generate HTML report

To maintain code quality, run flake8 with the following command:

flake8 --format=html --htmldir=flake8_reports

### Viewing the HTML Report

After running the command, an HTML report is generated in the `flake8_reports` directory. To view detailed flake8 analysis, follow these steps:

1. Navigate to the `flake8_reports` directory.
2. Locate and open `index.html` in a web browser.

## Conclusion

The Chess Tournament Management System is designed to be extensible and user-friendly, offering a comprehensive solution for managing chess tournaments, players, and generating detailed reports.



