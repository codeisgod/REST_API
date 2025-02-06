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