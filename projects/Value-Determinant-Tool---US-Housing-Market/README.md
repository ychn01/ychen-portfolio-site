# CSE6242 Spring 2023 Group Project Repo - Housing Market Analysis

CSE6242 Spring 2023 Group Project Repo - Housing Market Analysis
Team 74

## Description:

Our web application visualizes the Federal US Housing Price Index, as well as many other economic data features. These features can be selected, and unselected, to compare to the Housing Price Index. You can visually see how each timeseries data feature compares to the Housing Price Index by looking at the line plot, or you can look below the line plot for more detailed statistical analysis such as the most important features according to our linear regression model, or you can take a look at the correlation coefficient. If you would like more information on a certain state in the US, you can go over to the "Local Level Analysis" tab and take a look at more detailed data for each state. You can also change the date range to take a look at a specific time period.

## Installation:

Python version 3.x.x is required with several popular modules such as pandas, numpy, dash, datetime etc. 


## Execution:

 - First, navigate to "/CSE6242_GP/data_vis_app/", find "dash_backend.py", and open it in an IDE such as Spyder or Visual Studio Code, and run it. Or, navigate to the directory in a terminal with python available, and run "$ python dash_backend.py".
 - Then, open a web browser and go to http://localhost:8000/ to interact with the web application.

## Contributing

- Yu-Xi Chen, ychen3281, ychen3281@gatech.edu
- Team Members

## License

[None]


# App
- ToDo
  - [x] Get all data in the repo
  - [x] Normalize all data
  - [x] Add data filter functionality for each dataset
  - [x] Calculate Correlation Coefficients
  - [x] First: Find more data that correlates with housing price index (Government Policies/Subsidies? Consumer confidence polls?)
  - [x] Second: Create a predictor model with housing price index as the target variable
  - [x] Add date filter
  - [x] Add Region filter
  - [x] Update correlation table on filter
  - [x] Should we add a different tab for localized data? So one tab is US/Federal level and the other tab is local state or ZIP code level?
  - [x] Order the Correlation Coefficients in descending order
  - [x] Clean up the title of the graph
  - [x] Implement a predictor model on either federal or regional level (bigger task)
  - [x]  Calculate Correlation Coefficients for local data

