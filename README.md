# Spreadsheet Analysis Report
I analyzed a dataset of  England soccer games of the top four tiers from 1888 to 2020. The dataset originated from a Github published by DataHub, an organization that focuses on data management solutions. The format of the original data file that I downloaded was in .txt format. 

Below is an example of the dataset in its original format in table form:

|    | Date       | Season | home                    | visitor              | FT  | hgoal | vgoal | division | tier | totgoal | goaldif | result |
|----|------------|--------|-------------------------|----------------------|-----|-------|-------|----------|------|---------|---------|--------|
| 0  | 1888-09-08 | 1888   | Bolton Wanderers        | Derby County         | 3-6 | 3     | 6     | 1        | 1    | 9       | -3      | A      |
| 1  | 1888-09-08 | 1888   | Everton                 | Accrington F.C.      | 2-1 | 2     | 1     | 1        | 1    | 3       | 1       | H      |
| 2  | 1888-09-08 | 1888   | Preston North End       | Burnley              | 5-2 | 5     | 2     | 1        | 1    | 7       | 3       | H      |
| 3  | 1888-09-08 | 1888   | Stoke City              | West Bromwich Albion | 0-2 | 0     | 2     | 1        | 1    | 2       | -2      | A      |
| 4  | 1888-09-08 | 1888   | Wolverhampton Wanderers | Aston Villa          | 1-1 | 1     | 1     | 1        | 1    | 2       | 0       | D      |
| 5  | 1888-09-15 | 1888   | Aston Villa             | Stoke City           | 5-1 | 5     | 1     | 1        | 1    | 6       | 4       | H      |
| 6  | 1888-09-15 | 1888   | Blackburn Rovers        | Accrington F.C.      | 5-5 | 5     | 5     | 1        | 1    | 10      | 0       | D      |
| 7  | 1888-09-15 | 1888   | Bolton Wanderers        | Burnley              | 3-4 | 3     | 4     | 1        | 1    | 7       | -1      | A      |
| 8  | 1888-09-15 | 1888   | Derby County            | West Bromwich Albion | 1-2 | 1     | 2     | 1        | 1    | 3       | -1      | A      |
| 9  | 1888-09-15 | 1888   | Everton                 | Notts County         | 2-1 | 2     | 1     | 1        | 1    | 3       | 1       | H      |
| 10 | 1888-09-15 | 1888   | Wolverhampton Wanderers | Preston North End    | 0-4 | 0     | 4     | 1        | 1    | 4       | -4      | A      |
| 11 | 1888-09-22 | 1888   | Aston Villa             | Everton              | 2-1 | 2     | 1     | 1        | 1    | 3       | 1       | H      |
| 12 | 1888-09-22 | 1888   | Blackburn Rovers        | West Bromwich Albion | 6-2 | 6     | 2     | 1        | 1    | 8       | 4       | H      |
| 13 | 1888-09-22 | 1888   | Derby County            | Accrington F.C.      | 1-1 | 1     | 1     | 1        | 1    | 2       | 0       | D      |
| 14 | 1888-09-22 | 1888   | Preston North End       | Bolton Wanderers     | 3-1 | 3     | 1     | 1        | 1    | 4       | 2       | H      |
| 15 | 1888-09-22 | 1888   | Stoke City              | Notts County         | 3-0 | 3     | 0     | 1        | 1    | 3       | 3       | H      |
| 16 | 1888-09-22 | 1888   | Wolverhampton Wanderers | Burnley              | 4-1 | 4     | 1     | 1        | 1    | 5       | 3       | H      |
| 17 | 1888-09-29 | 1888   | Aston Villa             | Notts County         | 9-1 | 9     | 1     | 1        | 1    | 10      | 8       | H      |
| 18 | 1888-09-29 | 1888   | Bolton Wanderers        | Everton              | 6-2 | 6     | 2     | 1        | 1    | 8       | 4       | H      |
| 19 | 1888-09-29 | 1888   | Derby County            | Preston North End    | 2-3 | 2     | 3     | 1        | 1    | 5       | -1      | A      |
| 20 | 1888-09-29 | 1888   | Stoke City              | Accrington F.C.      | 2-4 | 2     | 4     | 1        | 1    | 6       | -2      | A      |

The original dataset, while formatted nicely and not consisting missing values, did consist of a lot of redundant or irrelevant data for the analysis I wanted to do. Additionally, as the original dataset was in .txt format, I utilized the Pandas package to initially convert the dataset into a DataFrame. Subsequently, as I wanted to focus on tier 1 games, I deleted all the games that were not in tier 1. Then, I deleted all the columns that I did not need for my analysis, which
are titled 'division', 'tier', and 'FT'. When converting the DataFrame into a CSV file, I encountered an issue that the conversion resulted in a column of indexes, which were not needed. As such, I had to explicitly write in my python program to make the first column the 'Season' column.

When doing the analysis of my spreadsheet, I decided to find the aggregate statistics that will help me visualize how significant home advantage is to a team's performance. At first, for aggregate statistics that do not require any conditions,I found the Average Home Goals Scored, Average Away Goals Scored, Highest Home Goals Scored in a Single Game, and Highest Away Goals Scored in a Single Game. The result of all those statistics favored the Home team. Afterwards, for
aggregate statistics with conditions, I found the Number of Home Wins, Number of Draws, Number of Away Wins, and Highest Amount of Total Goals Scored in a Draw. Following a similar pattern, I found that the number of home wins significantly outnumbered the number of draws and the number of away wins. 

As a result of the findings from those aggregate statistics, I was curious to see how home advantage has changed throughout the 130 years of soccer games I had in my polished dataset. So, I plotted the average goal difference by season in a line chart to see if there are any trends as time goes on (Goal Difference in a single game is calculated as home goals scored - away goals scored). 

Attached below is the following line chart:

![alt text](https://github.com/dbdesign-assignments-spring2022/spreadsheet-analysis-asakti47/blob/main/Home%20Advantage%20Line%20Chart.png)

As can be seen, home advantage exists in every single season except for seasons that never took place during the period
of World War I and World War II. It is also fascinating to see that the significance of home advantage seems to lessen as time goes on. A few ideas I have in mind that could explain that trend is the improvement in transportation methods, diet, and sports science.