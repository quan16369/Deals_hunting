# Deals Hunting

## Introduction

**Deals Hunting** is a project designed to automate the process of finding and collecting the best online shopping deals. By leveraging software agents, the system can browse various e-commerce websites, identify discounted or special deal products, and aggregate this information for easy user access.

## Tech Stack

- **Python**: Core programming language used.
- **Pushover**: For notifications on deals.
- **HuggingFace**: Used for NLP tasks in processing product descriptions.
- **Modal**: Cloud hosting solution.
- **OpenAI**: For AI-powered analysis and recommendations.
  
## Features

- **Web Scraping Agents**: Agents are deployed to browse e-commerce websites and collect data on discounted products.  
- **Pricing Model**: Uses a pricing model to evaluate the attractiveness of discovered deals.  
- **User Interface**: Provides an interface for users to view deals that have good prices through Gradio.  

## Agent Workflows
![image](https://github.com/user-attachments/assets/f0ca8309-f7aa-4ffb-a61c-5f7dd3e0a2c7)

1. **The UI**: Built using Gradio for user interaction.
2. **The Agent Framework**: Handles memory and logging for the agents.
3. **Planning Agent**: Coordinates activities among all agents.
4. **Scanner Agent**: Identifies promising deals from scraped data.
6. **Specialist Agent**: Estimates prices for specific categories.
7. **Ensemble Agent**: Combines insights from multiple agents to finalize price estimates.
8. **Messaging Agent**: Sends push notifications to users about exciting deals.
   
## Installation

1. **System Requirements**:
   - Python 3.9 or higher  
   - Libraries listed in the `environment.yml` file  

2. **Environment Setup**:
   - Create the environment using `conda`:  
     ```bash
     conda env create -f environment.yml
     ```  
   - Activate the environment:  
     ```bash
     conda activate llms
     ```  

## Usage

- Run the script `deal_hunting.py` to start collecting and analyzing deals:  
  ```bash
  python deal_hunting.py
  ```  
- Navigate to the provided Gradio link.
- Interact with the user-friendly interface to view deals.

## Project Structure

- `agents/`: Contains agents responsible for scraping different e-commerce websites.  
- `base_model/`: Includes the pricing model and data analysis tools.  
- `data_curation/`: Tools for processing and cleaning the collected data.  
- `fine_tuning/`: Methods for fine-tuning the model to improve performance.  
- `testing/`: Includes tests to ensure system quality and accuracy.

## Demo
```bash
python deals_hunting.py
```
![image](https://github.com/user-attachments/assets/5d69d44b-4b6b-4dfc-be0b-3123feed5b28)
