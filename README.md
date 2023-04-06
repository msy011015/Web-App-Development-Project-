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

   Upon building on the initial required function of "find_stop_near", we intended to scope our project by inocrporating additional functionalities like let the user choose their preferred mode of transportation and display real-time updates on the location of the bus, subway, or commuter rail. However, during the coding process, when we consistently receive an error message for getting nearest stop after selecting means of transportation, we discovered that the API itself already contains parameters on longitude, latitude, and distance (shown on [API GITHUB PAGE](https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index)). When we want to extract distance after selecting some dictionaries from the list and generate a new list, it is harder to extract the distance parameter. We have to calculate it by ourselves. So, we gave up this function and try perdiction of arrival time of next bus and time alert. We use “departure_time" in attributes for perdiction, and provide minutes_until_departure through calculating the time difference between current time and departure time. 

  
   


2. Discuss your **team's work division**, including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time.

3. Discuss from a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed. Consider including screenshots to demonstrate your project's progress and development.

**Note**: 
- Begin by including the names of all team members at the top of the document.
- Make the `README.md` file clear and concise. There is no need to use fancy words or ChatGPT. 
