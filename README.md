# WebApp-MBTA
 This is a repository for Charlotte Chen and Jenny Ma's Web App Developement project.

## Project Writeup and Reflection


**1. Project Overview**   

 This project develops a web application that leverages the Mapbox and MBTA APIs to determine the latitude and longitude of a user-specified location and identify the three nearest MBTA stops, along with their wheelchair accessibility status. Additionally, the application provides a predictive model for the next train departure time and how long it will be before the train leaves. Flask was utilized to create a user-friendly website that prompts the user for the desired location, and presents the 3 nearest MBTA stop information on a separate page, while also informing the user if no relevant MBTA stops were found. To enhance the user's experience, we have beautified the page with CSS by utilizing various colors, fonts, etc.

**2. Reflection** (~3 paragraphs + screenshots)

After you finish the project, Please write a short document for reflection.

1. Discuss the **process** point of view, including what went well and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped the team succeed.
   In the initial required process of finding nearest stop, 
   However, building upon the basic function find_stop_near, we want to enlarge the project scope through adding functions like find_stop_near after choosing the means of transportation the user wants and add a real-time showing where the bus is at. However, when we are writing the codes, we realized that the longitude and latitude retrivance and find nearest stop can be accomplished since the API itself contains these data and distance parameters according to the [API GITHUB PAGE](https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index). However, if we categorize the list of dictionaries and create a new list, we fail to get the distance. For the real-time tracker, we will need more inputs like destination (to clarify the bus with correct direction), which bus is preferable (there may be multiple routes to reach one destination) which will be much more complex and beyond our abilities.  


2. Discuss your **team's work division**, including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time.

3. Discuss from a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed. Consider including screenshots to demonstrate your project's progress and development.


 In this project, we found ChatGpt not very useful. Due to the project's numerous APIs and various types of documentation, we found it difficult to approach ChatGpt for the information we required. Instead of letting ChatGpt generate the code, we provided it with our code and asked it what the best approach was to achieve a particular goal, and then modifying it according to the provided method. Here is an example of the answer generated:
![images/general question.png](https://github.com/msy011015/Web-App-Development-Project-/blob/main/images/general%20question.png)
 
 However, ChatGpt is still a useful tool for learning new topics and debugging. While learning CSS, we questioned ChatGpt about expressions and what ChatGpt error messages signified.
![images/CSS.png](https://github.com/msy011015/Web-App-Development-Project-/blob/main/images/CSS.png)
![images/debug.png](https://github.com/msy011015/Web-App-Development-Project-/blob/main/images/debug.png)
![images/debug2.png](https://github.com/msy011015/Web-App-Development-Project-/blob/main/images/debug2.png)

