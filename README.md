# WhenWeMet
[//]: # "Contributors: Dhyey Patel, Nachiket Dighe, Nehang Patel, Saumick Pradhan, Tharun Ravi Kumar"

Have you ever found a need for an event planner for wedding? Was it really expensive to hire an event planner? Worry not, this repository consists of a software that helps you create the perfect wedding plan that fits your budget and time availabilty!

</br>

## Vision

#### Describe the top-level objectives, differentiators, target customers, and scope of your product.
* Our team is designing a dynamic software to recommend an optimal wedding plan using in-house machine learning methods. It will use a ML model to distribute the budget as per the user preferences and suggest a wedding plan with possible venues, caterers, cake bakeries, musicians, etc.
* The customer demographic for our software includes all the people who are looking to get married and for an event planner.
* The primary scope for this project is to target the audience within the Greater Cincinnati area.

#### What is your product (high-level view)?
* In this project, the user would be asked to input the budget of the wedding, time availabilty for the wedding, and preferences on events (such as priority venue and catering service).
* Our software would then calculate and distribute the budget to give an optimal wedding plan to the user. This will have recommendations for venues, caterers, musicians, etc.
* This would not be as expensive as hiring an event planner, as we would ask for a one time fee only. Our software would also give a wedding plan much quicker.

[//]: # "One time fee or Monthly subscription"
[//]: # "A one-time fee would make more sense, since people would just marry once in their life (generally speaking)."

#### Whom is it for?
* The target audience are people that are interested to have a wedding in Cincinnati.

#### What problems does it solve?
* Hiring an event planner is often too expensive.
* Hiring an event planner is also very time consuming.

[//]: # "Add your comments above!"

#### What alternatives are available, who are your competitors?
* Event Planners such as Zola, The Knot, WrightPlace Wright Event, etc.
* Event Planning Softwares like Hubilo, slido, eventsquid, etc.

#### What is novel in your approach, that is why is this project compelling and worth developing?
* We are applying ML methodologies to recommend choices for event planning, as per user preferences and their budget. It doesn't require the user to go through the extra hassle of hiring an event planner, and talking through what they prefer!

</br>

## Software Architecture

#### Make it clear that the system can be built, making good use of the available resources and technology.
* We will need to generate a dataset of all the service providers in the chosen local region. Then, we will generate recommendations based on a pre-trained model using the data we collected. We will use Google Cloud Platform to store our datasets and embeddings. 
* For the first iteration, we want to have a smaller text corpus. Our product will have a web interface and will be hosted on UC homepages server.  

#### Describe at a very high level the system's architecture, identifying the components/modules that will interact.
* The datasets created will have the search categories (eg. venues, caterers, cake bakeries, musicians, etc.) mapped with the costing options. After pre-preocessing the dataset, we will train our model on this corpus. The model will be trained and the embeddings will be saved on GCP. The user will enter their budget weights for each category, and our model will recommend the avaliable options based on that. 

#### Describe the specific data you will access/store.
* We will be storing data related to the different types of wedding “attributes” that people can potentially opt for based on their desired budget. We will include information about the available venues, caterers, event management services, decorators, etc., which the user can choose from based on what their budget is. We would provide all these services (listed in varying prices) and the user will be able to choose from them, according to their liking.

#### What languages/toolkits do you intend to use for the development?
* UI Tools (html, css, js), Visual Studio Code, Jupyter Notebook, Flask, etc.

</br>

## Challenges and Risks
#### What is the single most serious challenge you see in developing the product on schedule?
* One of the main challenges we would face if we developed the product on time is the UI and AWS development, because for a wedding planner website, we would need to ensure that the UI is appealing to the viewers/users, as well as collect information on the various weddings and build API's for using that information and connecting it to both, the frontend and backend of the software.

#### How will you minimize or mitigate the risk?
* To reduce the risk of UI and AWS development, we might begin by developing and upgrading our front and back ends using simple open source templates. This gives us a strong start and saves us time, allowing us to focus on building the program. This would also assist us in lowering our AWS consumption expenditures.
