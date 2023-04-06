# WebApp-MBTA
 This is a repository for Charlotte Chen and Jenny Ma's Web App Developement project.

## Project Writeup and Reflection


Write a summary of your project and your reflections on it in [`README.md`](README.md), using [Markdown format](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) (1 per team, not 1 per person).The [`README.md`](README.md) file should include the following sections:

**1. Project Overview** (~1 paragraph)

Write a short abstract describing your project. Include all the extensions to the basic requirements. 

**2. Reflection** (~3 paragraphs + screenshots)

After you finish the project, Please write a short document for reflection.

1. Discuss the **process** point of view, including what went well and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped the team succeed.
   In the initial required process of finding nearest stop, 
   However, building upon the basic function find_stop_near, we want to enlarge the project scope through adding functions like find_stop_near after choosing the means of transportation the user wants and add a real-time showing where the bus is at. However, when we are writing the codes, we realized that the longitude and latitude retrivance and find nearest stop can be accomplished since the API itself contains these data and distance parameters according to the [API GITHUB PAGE](https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index). However, if we categorize the list of dictionaries and create a new list, we fail to get the distance. For the real-time tracker, we will need more inputs like destination (to clarify the bus with correct direction), which bus is preferable (there may be multiple routes to reach one destination) which will be much more complex and beyond our abilities.  


2. Discuss your **team's work division**, including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time.

3. Discuss from a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed. Consider including screenshots to demonstrate your project's progress and development.

**Note**: 
- Begin by including the names of all team members at the top of the document.
- Make the `README.md` file clear and concise. There is no need to use fancy words or ChatGPT. 
