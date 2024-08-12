# Study_Students

  <h3 align="center">SMARTHOUSE_LIGHTS</h3>

<details open="open">
  <summary>Table of contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the project</a>
      <ul>
        <li><a href="#built-with">Built with</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

## About the project
This application provides a web-interface to control LED Lights connected to Raspberry Pico.

### Built with

* [Poetry](https://python-poetry.org/)
* [FastApi](https://fastapi.tiangolo.com/)

## Getting started

To get a local copy up and running follow these steps.

### Prerequisites

* Python
* pip
* Poetry (pip install poetry)

### Installation

**ALL FOLLOWED COMMANDS MUST BE USED IN PROJECT DIRECTORY**

1. Clone the repository
   ```sh
   git clone https://github.com/GASTER2302/Study_Students.git
   ```
2. Install python packages
   ```sh
   poetry install
   ```

3. Download MicroPython and load it to your Pico.

4. Load files from Pico directory to your Pico.

## Usage

To start the application in VS Code:

    1. Add poetry virtual interpritator as your interpritator.

    2. Change COM Port to the port you connected to the Pico.

    3. Change Pin and count of LEDs on led_strip_controller.py file at your Pico.

    4. Start the application:

    ```sh
    python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

    5. Go to localhost:8000 and enjoy!
