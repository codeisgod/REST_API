# REST_API
- `REST` stands for `RE`presentational `S`tate `T`ransfer.
- `API` stands for `A`pplication `P`rogramming `I`nterface
- `REST APIs` are those APIs which follow the guidelines set by the REST architecture.
    - They follow a client-server model where one software program sends a request and the other responds with some data.
    - REST APIs commonly use the HTTP protocol to send requests & receive responses.
    <br>
    - HTTP requests for webpages return HTML, CSS & JavaScript files which are rendered by the browser and displayed to the user.  
    - But, in the case of APIs, the request can be for any data (not just webpage) and the response is read by the requesting program which interprets the data.
    - Respose is in JSON 
    - JSON (JavaScript Object Notation) is a standard data format that is easily “understandable” by applications
        - It can be handled well in most languages
        - So the data format in REST is usually JSON
        - For example, an Android app can effortlessly utilize data sent by a Node.js server

**Tips:**
XML is another popular format for data transfer between applications.

## Components of a REST API endpoint
- Install [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) chrome extension or a similar tool to automatically format the JSON response in your browser window
- Here’s a visual on different parts of an API endpoint.
    - The root endpoint will be the same for all API endpoints supported by a provider
    - The API path specifies the resource to be fetched (eg: videos, users)
    - Path parameter is used to identify and return a specific resource
    - Query parameter is used to filter or search for resources
    - Example [EPI_EndPoint](./API_EndPoint.png)
    <br>
    - For an API that needs to take two search parameters - genres and contentRating, the request URL should be like this https://crio-xflix.herokuapp.com/v1/videos?genres=Movies&contentRating=12%2B
        - Note: Here, 12%2B is the url encoded version of “12+”. Special characters like “+” need to be encoded as they have other meanings when used in a URL.

## REST and HTTP
- REST API calls are made on top of the HTTP protocol. 
- We can analyse the network packets during the API calls to confirm this using **Wireshark**.
    - Wireshark is a popular network analysis tool to capture network packets and display them at a granular level. Once these packets are broken down, you can use them for real-time or offline analysis.

**Tips**
REST is one architectural pattern used, NOT the only one. There are some has-beens, like SOAP and some new kids on the block, like GraphQL. These patterns differ in the ways in which they ask for data, send data, and how they enforce these practices.

### Visualizing API request-response packets using Wireshark
- From analysing the [Wireshark](./wireShark.png) data given above, we can understand that
    -   The client sends a HTTP GET request (Entry No. 66) to the server for the resource at /v1/videos/60331f421f1d093ab5424489 (API request was made to https://content-xflix-backend.azurewebsites.net/v1/videos/60331f421f1d093ab5424489)
    - The server responds with a 200 status code and JSON data on line 77.
    - You’ll find the Hypertext Transfer Protocol (HTTP) being used for communication
    - The JSON data returned is formatted and displayed in the lower pane

## REST API calls using Programs
1. Execute the below `curl` command on the terminal to make a REST API call to https://content-xflix-backend.azurewebsites.net/v1/videos/60331f421f1d093ab5424489
```
curl https://content-xflix-backend.azurewebsites.net/v1/videos/60331f421f1d093ab5424489
```
2. create new file in Java/Python
    - Choose your pick from Java / Python to fetch API data using one of these languages.
    - Python
        - copy code from [main.py](./main.py)
        - Open terminal and then run the following commands:
        ```
        python3 main.py
        ```
    - Java
        - copy code from [main.java](./main.java)
        - Open terminal and then run the following commands:
        ```
        java main.java
        ```

## More Reading

- Here are some more APIs if you’d like to explore
    - [Crypto data API](https://docs.cryptowat.ch/rest-api/)
    - [Stock data API](https://www.alphavantage.co/documentation/)
- Further Reading (Optional)
    - [Understanding And Using REST APIs](https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/) 
    - [JSON in 10 minutes](https://www.youtube.com/watch?v=iiADhChRriM)
    - [Path parameter vs Query parameter](https://medium.com/@fullsour/when-should-you-use-path-variable-and-query-parameter-a346790e8a6d)
    - [Idempotency in REST APIs](https://www.restapitutorial.com/lessons/idempotency.html)
    - [Capturing HTTP network packets using Wireshark](https://en.wikiversity.org/wiki/Wireshark/HTTP)