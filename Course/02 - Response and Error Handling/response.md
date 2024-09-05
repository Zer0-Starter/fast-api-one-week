# Response model and Error handling

## Response

The response have two part, Header ans Body. The header gives the request status and additional information to guide the delivery of the response body. One example is 'Content-Type' which tells the client the content type returned. The response body is the data requested from the server by the client.

### Status code:

+ 1XX: Request has been received
+ 2XX: The request was succesful
+ 3XX: Request redirected
+ 4XX: There's an error from the client
+ 5XX: There's an error from the server

## Eror 

To handdle error in FastAPI, we use HTTPException class. It indicates a fault or issue in the request flow.
