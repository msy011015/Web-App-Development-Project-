# WebApp-MBTA
 This is a repository for Charlotte Chen and Jenny Ma's Web App Developement project.

## Project Writeup and Reflection


**1. Project Overview**   

 This project develops a web application that leverages the Mapbox and MBTA APIs to determine the latitude and longitude of a user-specified location and identify the three nearest MBTA stops, along with their wheelchair accessibility status. Additionally, the application provides a predictive model for the next train departure time and how long it will be before the train leaves. Flask was utilized to create a user-friendly website that prompts the user for the desired location, and presents the 3 nearest MBTA stop information on a separate page, while also informing the user if no relevant MBTA stops were found. To enhance the user's experience, we have beautified the page with CSS by utilizing various colors, fonts, etc.

**2. Reflection** (~3 paragraphs + screenshots)

After you finish the project, Please write a short document for reflection.

1. Discuss the **process** point of view, including what went well and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped the team succeed.

   The initial required process of finding nearest stop and make the website went well smoothly. Upon building on the initial required function of "find_stop_near", we intended to scope our project by inocrporating additional functionalities like let the user choose their preferred mode of transportation and display real-time updates on the location of the bus, subway, or commuter rail. However, during the coding process, when we consistently receive an error message for getting nearest stop after selecting means of transportation, we discovered that the API itself already contains parameters on longitude, latitude, and distance (shown on [API GITHUB PAGE](https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index)). When we want to extract distance after selecting some dictionaries from the list and generate a new list, it is harder to extract the distance parameter. We have to calculate it by ourselves. So, we gave up this function and try perdiction of arrival time of next bus and time alert. We use “departure_time" in attributes for perdiction, and provide minutes_until_departure through calculating the time difference between current time and departure time. We efficiently used agile management, so that we can find some functions infeasible and drop it immediately after several rounds of testing. 


2. Discuss your **team's work division**, including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time.

3. Discuss from a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed. Consider including screenshots to demonstrate your project's progress and development.

 From a learning perspective, we learned how to access web data programmatically by locating APIs on the internet and understanding their functions according to the instructions. This enables us to visit any website in the future, locate the pertinent APIs, and present the data in Python. Flask is a valuable utility for developing simple websites. It can be utilized as an MVP rendering, with CSS and other extensions assisting in the enhancement of web pages.

We observed that in addition to these fundamental tools, there were SQL, Bootstrap, jQuery, as well as other skills we had not acquired. If we had known about them beforehand, we would have liked more time to learn each of them, as they would have helped us create a more professional website and enhance the user experience, as opposed to the simpler framework we have now.

 In this project, we found ChatGpt not very useful. Due to the project's numerous APIs and various types of documentation, we found it difficult to approach ChatGpt for the information we required. Instead of letting ChatGpt generate the code, we provided it with our code and asked it what the best approach was to achieve a particular goal, and then modifying it according to the provided method. Here is an example of the answer generated:

![images/general question.png](https://github.com/msy011015/Web-App-Development-Project-/blob/main/images/general%20question.png)
 
 However, ChatGpt is still a useful tool for learning new topics and debugging. While learning CSS, we questioned ChatGpt about expressions and what ChatGpt error messages signified.

![images/CSS.png](https://github.com/msy011015/Web-App-Development-Project-/blob/main/images/CSS.png)
![images/debug.png](https://github.com/msy011015/Web-App-Development-Project-/blob/main/images/debug.png)
![images/debug2.png](https://github.com/msy011015/Web-App-Development-Project-/blob/main/images/debug2.png)

