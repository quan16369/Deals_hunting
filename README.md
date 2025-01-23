# Deals Hunting

## Introduction

**Deals Hunting** is a project designed to automate the process of finding and collecting the best online shopping deals. By leveraging software agents, the system can browse various e-commerce websites, identify discounted or special deal products, and aggregate this information for easy user access.

## Features

- **Web Scraping Agents**: Agents are deployed to browse e-commerce websites and collect data on discounted products.  
- **Pricing Model**: Uses a pricing model to evaluate the attractiveness of discovered deals.  
- **User Interface**: Provides an interface for users to view and filter deals based on their preferences.  

## Installation

1. **System Requirements**:
   - Python 3.8 or higher  
   - Libraries listed in the `environment.yml` file  

2. **Environment Setup**:
   - Create the environment using `conda`:  
     ```bash
     conda env create -f environment.yml
     ```  
   - Activate the environment:  
     ```bash
     conda activate deals_hunting
     ```  

## Usage

- Run the script `deal_hunting.py` to start collecting and analyzing deals:  
  ```bash
  python deal_hunting.py
  ```  
- Results will be saved in the `results/` directory as CSV files.  

## Project Structure

- `agents/`: Contains agents responsible for scraping different e-commerce websites.  
- `base_model/`: Includes the pricing model and data analysis tools.  
- `data_curation/`: Tools for processing and cleaning the collected data.  
- `fine_tuning/`: Methods for fine-tuning the model to improve performance.  
- `testing/`: Includes tests to ensure system quality and accuracy. 
![image](https://github.com/user-attachments/assets/5d69d44b-4b6b-4dfc-be0b-3123feed5b28)
